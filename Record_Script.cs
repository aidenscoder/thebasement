using System;

public record point(float x, float y);

class Program{
    public static void main(){
        Console.Readline("hello world");
        point my_point = new(12,16);
    }
}
