import { describe, it, expect } from '@jest/globals';
import { sum, sumParam, sumRest, sumExample, multiply, subtract } from '../src/arithematic'

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