-- Read a file and print each line on the stdout
-- first check if file exist or not

local function check_file(filepath)
	local file, error = io.open(filepath, "r")
	if file then
		file:close()
		return true
	else
		print("File doesn't exist: " .. error)
		return false
	end
end

local function read_lines(filepath)
	local file_exists = check_file(filepath)
	if file_exists then
		local file = io.open(filepath, "r")
		if file then
			for line in file:lines() do
				print(line)
			end
		end
	end
end

local filepath = os.getenv("HOME") .. "/github/exmpls/lua-exmpls/scripts/ex1.lua"
read_lines(filepath)
