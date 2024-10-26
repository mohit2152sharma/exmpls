# Numbers in javascript

```javascript
// the syntax is: [digits][.digits][(E|e)[+|-]digits]
3.15;
3;
6e24;
1.4e-12;

// separators is optional
let billion = 1_000_000_000;
let bytes = 0b1000_0000;

// supports basic arithemetic
// + for addition, - for subtraction, * for multiplication, ** for exponents, / for division, % for modulo

// When result is larger than largest representable value (overflow), returns +Infinity
1e1000 - // returns Infinity
  // When result is smaller than smallest representable value, returns -Infinity
  1e1000; // returns -Infinity

// underflow occurs when result is closer to zero, returns zero
1e-1000 - // returns 0
  // when result is close to zero from a negative number, returns -zero
  1e-1000; // returns -0

// Division by zero is not an error, It returns Infinity or -Infinity
1 / 0 - // returns Infinity
  1 / 0; // returns -Infinity

// Zero divided by zero returns NaN
0 / 0; // returns NaN

// NaN also arises for following cases
Infinity / Infinity; // returns NaN
"hello" * 2; // returns NaN
NaN + 1; // returns NaN
Infinity - Infinity; // returns NaN

// NaN does not compare equal to any other value including itself
NaN === NaN; // returns False
// Use Number.isNaN or isNaN to check for NaN
Number.isNaN(NaN); // returns True

// Infinity compares equal to itself
(Infinity ===
  Infinity - // returns True
    // Negative zero compares equal to positive zero, but not when used divisor
    0) ===
  0; // returns True
1 / -0 === 1 / 0; // returns False, -Infinity and Infinity are not equal

// More complex math features are included in Math object
Math.power(2, 23);
Math.random();

// Properties like Infinity, NaN are available as properties of Number object
Number.POSITIVE_INFINITY;
Number.MAX_VALUE;
Number.MIN_VALUE;
Number.parseInt();
Number.parseFloat();
Number.isNaN();
Number.isInteger();
Number.isFinite();
```
