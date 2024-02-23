// Define an enum Message
#[derive(Debug)]
enum Message {
    ChangeColor(i32, i32, i32), // Variant with three integers
    Echo(String),               // Variant with a String
    Quit,                       // Variant with no associated data
}

fn main() {
    // Example usage of each variant of the Message enum
    let change_color_message = Message::ChangeColor(255, 200, 100);
    let echo_message = Message::Echo(String::from("Hello, world!"));
    let quit_message = Message::Quit;

    // Print each message
    println!("ChangeColor: {:?}", change_color_message);
    println!("Echo: {:?}", echo_message);
    println!("Quit: {:?}", quit_message);
}
