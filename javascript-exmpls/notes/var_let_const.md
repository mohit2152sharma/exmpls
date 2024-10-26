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
