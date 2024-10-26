# lua in one page

> [!NOTE]
> Work in progress

- [ ] Add examples
- [ ] Add more details

## data types

### Bools

- Booleans are represented by `true` and `false`.
- Everything is considered truthy, except `false` and `nil`. Empty [`tables`](#tables), [`strings`](#strings), `0` evaluate to True, if used in `if/else` condition.

### Strings

- Concatenate two strings using `..` (two dots) i.e. `"hello" .. "world"`

### Tables

- tables are created using `{}`
- tables can be array like `{1, 2, 3, 4}` or a dictionary (or map) like `{a=1, b=2}` or both like `{1, 2, 3, a=1, b=2}`
- tables can be nested like `{1, 2, {1, 2, {a=1}}}`
- Elements from tables can be extracted by (assuming `t = {1, 2, a=1}`)
  - dot syntax i.e. `t.a`
  - using square brackets with:
    - key name e.g. `t["a"]`
    - array index e.g. `t[1]`
  - Only array elements have the index, key-value pairs don't
  - arrays are 1 indexed (not zero)

### Control Structures

#### if/else

- `if/else` syntax:

  ```lua
  if <condition> then
      <do something>
  elseif <condition> then
      <do something else>
  else
      <do something>
  end

  # or
  if <condition> then <do something> end
  if <condition> then <do something> else <do something else> end
  ```

#### while

- `while` syntax:

  ```lua
  local i = 1
  while i <= 10 do
      print(i)
      i = i + 1
  end
  ```

#### repeat until

- `repeat until` syntax:

  ```lua
  local i = 1
  repeat
      print(i)
      i = i + 1
  until i > 10
  ```

- Repeat a statement until a condition is true.
- In Lua the scope of a local variable declared inside the loop includes the condition.

  ```lua
  local x = 100
  local sqrt = x / 2
  repeat
    sqrt = (sqrt + x / sqrt) / 2
    local error = math.abs(sqrt ^ 2 - x)
  until error < x / 10000 -- the local error defined above is visible here
  ```

### functions

- ```lua
    x = function(param)
        <do something>
    end
  ```

### Scopes

- You created variables in local scope using `local` keyword e.g. `local var = 1`
- By default, if variables are created without `local` keyword, then variables are created in global scope
