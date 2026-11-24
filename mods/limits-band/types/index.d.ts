export type Limit = { percentUsed: number; resetsAt?: string }
export type Limits = { fiveHour: Limit | null; sevenDay: Limit | null }

declare module 'claude-code' {
  interface PluginState {
    'limits-band': { limits: Limits }
  }
}
