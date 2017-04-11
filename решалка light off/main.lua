
require "plase"
require "instruction"

function love.load()
	IN_PROCESS = plase.load()
end

function love.mousepressed(x,y,botton)
	IN_PROCESS.mousepressed(x,y,botton)
end

function love.mousereleazed(x,y,botton)
	IN_PROCESS.mousereleazed(x,y,botton)
end

function love.update(dt)
	IN_PROCESS.update(dt)
end

function love.draw()
	plase.draw()
	instruction.draw()
end