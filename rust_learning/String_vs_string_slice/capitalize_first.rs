pub fn capitalize_first(input: &str) -> String {
    let mut c = input.chars();
    match c.next() {
        None => String::new(),
        Some(first) => first.to_uppercase().to_string(),
        // Some(first) => {
        //     let mut result = first.to_uppercase().to_string(); // Capitalize the first character and convert it to a String
        //     result.extend(c); // Extend the result with the remaining characters
        //     result // Return the resulting string
        // }
    }
}

fn main() {
    let text= capitalize_first("hello");
    println!("text: {}", text)
}