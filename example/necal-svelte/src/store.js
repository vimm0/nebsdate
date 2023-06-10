import { writable, readable } from 'svelte/store'

export const currentYearMonthState = writable('')

export const yearsState = readable([], async (set) => {
  try {
    const response = await fetch('/data/years.json')
    if (response.ok) {
      const data = await response.json()
      console.log(data)
      set(data)
    }
  } catch (error) {
    console.error(error)
  }

  // Return the unsubscribe function which doesn't do anything here (but is part of the stores protocol).
  return () => undefined
})
