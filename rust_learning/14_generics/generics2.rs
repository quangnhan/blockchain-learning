use std::fmt::Display;

// Generic Struct Definition, T is a variable for unknown type
struct Stats<T> {
    age: T,
    height:T
}

// Impl blocks defining methods for different types
impl<T:Display> Stats<T> {
  fn print_stats(&self){
    println!("Age is {} years and Height is {}", self.age, self.height);
  }
}


fn main() {
    // Instantiate using i32 stats
    let alex = Stats {age: 37, height: 70};
    // Instantiate using f32 stats
    let alex2 = Stats {age: 37.0, height: 5.83};
    // Instantiate using String stats
    let alex3 = Stats {age: "37".to_string(), height: "5'10ft".to_string()};
    // Call methods
    alex.print_stats();
    alex2.print_stats();
    alex3.print_stats();
}