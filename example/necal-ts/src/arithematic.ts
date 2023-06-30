// SUM
export function sum(a: number, b: number): number {
    return a + b;
}


export function sumParam(a: number, b: number, c: number): number {
    return a + b + c;
}

export function sumRest(...numbers: number[]): number {
    return numbers.reduce((total, current) => total + current, 0);
}

type ABC = { a: number; b: number; c: number };

export function sumExample({ a, b, c }: ABC) {
    return a + b + c;
}

// MULTIPLICATION
export function multiply(a: number, b: number): number {
    return a * b;
}

// SUBTRACTION
export function subtract(a: number, b: number): number {
    return a - b;
}