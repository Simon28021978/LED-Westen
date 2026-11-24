import type { Register } from 'claude-code'

const NAME = 'Simon'
const GOLD = '#D4AF37'
const OWN = new Set(['composer', 'bridge', 'sdk'])

export const register: Register = on => {
  on('ui.render', { component: 'UserMessage' }, async ($, e, next) => {
    if (!OWN.has(e.props.origin.kind) || e.props.from) return next(e)
    const row = await next(e)
    const { Box, Text } = $.ui.resolve(e)
    return (
      <Box flexDirection="column" borderStyle="round" borderColor={GOLD} paddingX={1}>
        <Text bold color={GOLD}>{NAME}</Text>
        {row}
      </Box>
    )
  })
}
