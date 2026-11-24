import type { Register } from 'claude-code'

const NAME = 'Simon'
const OWN = new Set(['composer', 'bridge', 'sdk'])

export const register: Register = on => {
  on('ui.render', { component: 'UserMessage' }, async ($, e, next) => {
    if (!OWN.has(e.props.origin.kind) || e.props.from) return next(e)
    const row = await next(e)
    const { Box, Text } = $.ui.resolve(e)
    return (
      <Box flexDirection="column">
        <Text bold color="cyan">{NAME}</Text>
        {row}
      </Box>
    )
  })
}
