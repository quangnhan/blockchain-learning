// Generic Struct Definition, T is a variable for unknown type
struct Stats<T> {
    age: T,
    height:T
}

// Impl blocks defining methods for different types
impl Stats<i32> {
  fn print_stats(&self){
    println!("Age is {} years and Height is {} inches", self.age, self.height);
  }
}

impl Stats<f32> {
  fn print_stats(&self){
    println!("Age is {} years and Height is {} feet", self.age, self.height);
  }
}


fn main() {
    // Instantiate using i32 stats
    let alex = Stats {age: 37, height: 70};
    // Instantiate using f32 stats
    let alex2 = Stats {age: 37.0, height: 5.83};
    // Call methods
    alex.print_stats();
    alex2.print_stats();
}