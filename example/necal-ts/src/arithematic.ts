export function sum(a: number, b: number): number {
    return a + b;
}


export function sumParam(a: number, b: number, c: number): number {
    return a + b + c;
}

export function sumRest(...numbers: number[]): number {
    return numbers.reduce((total, current) => total + current, 0);
}