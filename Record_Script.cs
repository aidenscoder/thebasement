using System;

public record point(float x, float y);

class Program{
    public static void main(){
        Console.WriteLine("hello world");
        point my_point = new(12,16);
        Console.WriteLine($"{my_point}");
    }
}
