fn main() {
    let mut s = String::new();
    
    // Using String
    let start = std::time::Instant::now();
    for _ in 0..1_000_000_000 {
        s += "hello";
    }
    println!("Time taken using String: {:?}", start.elapsed());
    
    // Using &str
    let mut s2 = String::new();
    let start = std::time::Instant::now();
    for _ in 0..1_000_000_000 {
        s2.push_str("hello");
    }
    println!("Time taken using &str: {:?}", start.elapsed());
}
