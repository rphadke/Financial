# The Hello Class
class Hello
   
   def initialize( name )
      @name = name.capitalize
   end

   def salute
      puts "Hello #{@name}!"
   end
   
end

h = Hello.new("Ruby")
h.salute

