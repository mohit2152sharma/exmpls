# Javascript Examples


<details>

<summary>`var`, `let` and `const`</summary>

# `var`, `let` and `const`

- All three keywords are used to create/declare variables in javascript.

## hoisting

- Hoisting in JavaScript is a behavior where variable and function declarations are moved to the top of their containing scope during the compilation phase, before the actual code execution.

    ```javascript
    // even though x is not defined yet, it will run without an error and print undefined
    console.log(x);

    var x = "hello";

    console.log(x); // this will print 'hello'

    // the above is equivalent to 
    var x;
    console.log(x);
    var x = "hello";
    console.log(x);
    ```

- For functions, in the following example, `somefunc()` is hoisted to the top, allowing it to be called before the actual function declaration in the code.

    ```javascript
    somefunc() // this will print 'hello' 

    function somefunc() {
        console.log('hello')
    }
    ```

## `const`

- A variable declared with `const` keyword, cannot be redeclared or reassigned (or updated).

    ```javascript
    const x = 1;

    const x = 2; // this will throw an error

    x = 3; // this will also throw an error
    ```

- `const` declarations are also hoisted but are not initialised until the interpreter reaches the actual declaration in the code, leading to a `ReferenceError` if used before initialization.

## `var` 

- The scope of variable declared with `var` is global, if it is declared outside of function. And it is function scoped, if it is declared inside function. 

    ```javascript

    function sayHello() {
        var x = 'hello'
    }

    sayHello()
    console.log(x) // this will print 'hello'
    ```

- The variables declared with `var` can be redeclared, reassigned and updated. 

    ```javascript
    var x = 'hello'
    var x = 'world'
    x = 'new'
    // none of the above throws error
    ```

- variables are hoisted. 

    ```javascript
    console.log(x) // prints undefined 
    var x = 'hello'
    console.log(x) //prints 'hello'
    ```

## `let` 

- variables declared with `let` keyword are block scoped. If the variable is used outside of block, it throws an error unlike `var`. 

    ```javascript
    function sayHello() {
        let x = 'hello'
    }
    sayHello()
    console.log(x) // this will throw ReferenceError

    function sayHello() {
        var x = 'hello'
    }
    sayHello() 
    console.log(x) // this will not throw a ReferenceError and prints 'hello'
    ```

- variables are hoisted, but they are only initialised when interpreter reaches the declaration. If the variables are used before initialised, it will throw a `ReferenceError` unlike `var`.

    ```javascript
    console.log(x) 
    let x = 'hello'
    ```

- variables declared with `let` keyword can be reassigned (or updated) but they cannot be redeclared. 

    ```javascript
    let x = 'hello'
    x = 'yellow' // allowed 
    let x = 'world' // not allowed
    ```

</details>

<details>

<summary>Numbers in javascript</summary>

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

// Division by zero is not an error, returns Infinity or -Infinity
1 / 0; // returns Infinity
-1 / 0; // returns -Infinity

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

</details>