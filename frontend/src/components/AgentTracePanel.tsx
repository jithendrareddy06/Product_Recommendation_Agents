import { useState } from 'react'
import type { AgentTraceStep } from '../types'

interface AgentTracePanelProps {
  trace: AgentTraceStep[]
}

export function AgentTracePanel({ trace }: AgentTracePanelProps) {
  const [open, setOpen] = useState(false)
  if (trace.length === 0) return null

  return (
    <section className="panel trace-panel">
      <button type="button" className="trace-toggle" onClick={() => setOpen((v) => !v)}>
        Agent steps {open ? '▲' : '▼'}
      </button>
      {open && (
        <ol className="trace-list">
          {trace.map((step) => (
            <li key={`${step.agent}-${step.summary}`}>
              <strong>{step.agent}</strong>: {step.summary}
            </li>
          ))}
        </ol>
      )}
    </section>
  )
}
