import { atom, read, update } from 'claude-code'
import type { EngineInterface, Register, SessionRateLimit } from 'claude-code'

import type { Limit, Limits } from '../types'

const EMPTY: Limits = { fiveHour: null, sevenDay: null }
const limits = atom({ plugin: 'limits-band', key: 'limits' } as const, EMPTY)

const pick = (rl: SessionRateLimit[], kind: string): Limit | null => {
  const w = rl.find(r => r.kind === kind)
  return w ? { percentUsed: w.percentUsed, resetsAt: w.resetsAt } : null
}

const fmtReset = (iso?: string): string => {
  if (!iso) return ''
  const d = new Date(iso)
  if (isNaN(d.getTime())) return ''
  const two = (n: number) => String(n).padStart(2, '0')
  const days = ['So', 'Mo', 'Di', 'Mi', 'Do', 'Fr', 'Sa']
  return ` (Reset ${days[d.getDay()]} ${two(d.getHours())}:${two(d.getMinutes())})`
}

const fmt = (label: string, l: Limit | null): string =>
  `${label}: ${l ? `${Math.round(l.percentUsed)}%${fmtReset(l.resetsAt)}` : '–'}`

const line = (l: Limits): string => `${fmt('5h', l.fiveHour)} · ${fmt('Woche', l.sevenDay)}`

async function refresh($: EngineInterface, rl: SessionRateLimit[]) {
  const next: Limits = { fiveHour: pick(rl, 'five_hour'), sevenDay: pick(rl, 'seven_day') }
  await update($, limits, () => next)
  $.ui.status(line(next))
}

export const register: Register = on => {
  on('session.start', async ($, e, next) => {
    const r = await next(e)
    await refresh($, (await $.session.usage()).rateLimits)
    return r
  })

  on('session.measure', async ($, e, next) => {
    if (e.changed.includes('rateLimits')) await refresh($, e.rateLimits)
    return next(e)
  })

  on('ui.render', { component: 'AbovePrompt' }, async ($, e, next) => {
    if (e.props.hasSurvey) return next(e)
    const l = await read($, limits)
    const { Box, Text } = $.ui.resolve(e)
    return (
      <Box>
        <Text dimColor>{line(l)}</Text>
      </Box>
    )
  })
}
