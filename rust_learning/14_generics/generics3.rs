struct Pair<T, U> {
    first: T,
    second: U,
}

impl<T> Pair<T, T> {
    fn are_equal(&self) -> bool {
        self.first == self.second
    }
}

fn main() {
    let pair1 = Pair { first: 5, second: 5 };
    let pair2 = Pair { first: "hello", second: "world" };
    let pair3 = Pair { first: 42, second: 27 };

    println!("Pair 1 equal? {}", pair1.are_equal()); // Prints: Pair 1 equal? true
    // println!("Pair 2 equal? {}", pair2.are_equal()); // This will fail to compile
    // println!("Pair 3 equal? {}", pair3.are_equal()); // This will fail to compile
}
