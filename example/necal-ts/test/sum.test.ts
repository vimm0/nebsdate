import {expect, test} from '@jest/globals';

// const sum = require('../src/counter');
import {sum} from '../src/counter'

test('adds 1 + 2 to equal 3', () => {
  expect(sum(1, 2)).toBe(3);
});