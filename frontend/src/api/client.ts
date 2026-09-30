import type { ShopResponse } from '../types'

const API_BASE = import.meta.env.VITE_API_URL ?? ''

export async function shopSearch(query: string): Promise<ShopResponse> {
  const res = await fetch(`${API_BASE}/api/shop`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ query }),
  })
  if (!res.ok) {
    const body = await res.text()
    if (res.status === 502 || res.status === 503) {
      throw new Error(
        'Cannot reach the ShopEasy API. Start the backend: cd backend, then run uvicorn app.main:app --reload --host 127.0.0.1 --port 8000',
      )
    }
    throw new Error(body || `Request failed (${res.status})`)
  }
  return res.json() as Promise<ShopResponse>
}
