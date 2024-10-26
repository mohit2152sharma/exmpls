local x = 100
local sqrt = x / 2
repeat
  sqrt = (sqrt + x / sqrt) / 2
  local error = math.abs(sqrt ^ 2 - x)
until error < x / 10000 -- the local error defined above is visible here
