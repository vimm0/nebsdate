import { describe, it, expect } from '@jest/globals';
import { sum, sumParam, sumRest } from '../src/arithematic'

describe('sum function', () => {
  it('should return addition of numbers', () => {
    expect(sum(1, 2)).toBe(3);
    expect(sumParam(1, 2, 3)).toBe(6);
    expect(sumRest(1, 2, 3)).toBe(6);

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