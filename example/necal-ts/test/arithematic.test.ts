import { describe, it, expect } from '@jest/globals';
import { sum, sumParam, sumRest, sumExample, multiply, subtract, divide, simplifyExpression } from '../src/arithematic'

describe('sum function', () => {
  it('should return addition of numbers', () => {
    expect(sum(1, 2)).toBe(3);
    expect(sumParam(1, 2, 3)).toBe(6);
    expect(sumRest(1, 2, 3)).toBe(6);
    expect(sumExample({ a: 1, b: 2, c: 3 })).toBe(6);

  });
  it('should return the correct sum for multiple numbers', () => {
    expect(sumRest(1, 2, 3)).toBe(6);
    expect(sumRest(4, 5, 6, 7)).toBe(22);
    expect(sumRest(-1, 2, -3, 4)).toBe(2);
  });

  it('should return the number itself if only one number is provided', () => {
    expect(sumRest(10)).toBe(10);
    expect(sumRest(-5)).toBe(-5);
  });

  it('should return 0 if no arguments are provided', () => {
    expect(sumRest()).toBe(0);
  });
});

describe('multiply', () => {
  it('should return the product of two numbers', () => {
    expect(multiply(2, 3)).toBe(6);
    expect(multiply(0, 10)).toBe(0);
    expect(multiply(-5, 4)).toBe(-20);
  });
});

describe('subtract', () => {
  it('should return the difference between two numbers', () => {
    expect(subtract(5, 3)).toBe(2);
    expect(subtract(10, 5)).toBe(5);
    expect(subtract(8, -2)).toBe(10);
  });
});

describe('divide', () => {
  it('should return the quotient of two numbers', () => {
    expect(divide(10, 2)).toBe(5);
    expect(divide(8, 4)).toBe(2);
    expect(divide(15, 3)).toBe(5);
  });

  it('should throw an error when dividing by zero', () => {
    expect(() => divide(10, 0)).toThrowError('Division by zero is not allowed.');
  });
});

describe('evaluateExpression', () => {
  it('should correctly evaluate the expression using BODMAS rule', () => {
    expect(simplifyExpression('2 + 3 * 4')).toBe(14); // Multiplication is evaluated first: 3 * 4 = 12, then addition: 2 + 12 = 14
    expect(simplifyExpression('(2 + 3) * 4')).toBe(20); // Parentheses enforce the order of evaluation: 2 + 3 = 5, then multiplication: 5 * 4 = 20
    expect(simplifyExpression('10 / 2 + 5 * 2')).toBe(15); // Division is evaluated first: 10 / 2 = 5, then multiplication: 5 * 2 = 10, and finally addition: 5 + 10 = 15
    expect(simplifyExpression('(10 / (2 + 3)) * 4')).toBe(8); // Parentheses enforce the order of evaluation: 2 + 3 = 5, then division: 10 / 5 = 2, and finally multiplication: 2 * 4 = 8
  });
});