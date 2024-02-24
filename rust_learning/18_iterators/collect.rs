fn main() {
    let numbers = vec![1, 2, 3, 4, 5];

    // Collect into a Vec<i32>
    let collected_vec: Vec<i32> = numbers.iter().map(|&x| x * 2).collect();
    println!("Collected into Vec<i32>: {:?}", collected_vec);

    // Collect into a Vec<Option<i32>>
    let collected_option_vec: Vec<Option<i32>> = numbers.iter().map(|&x| Some(x * 2)).collect();
    println!("Collected into Vec<Option<i32>>: {:?}", collected_option_vec);

    // Collect into a HashMap<i32, i32>
    let collected_map: std::collections::HashMap<i32, i32> = numbers.iter().map(|&x| (x, x * 2)).collect();
    println!("Collected into HashMap<i32, i32>: {:?}", collected_map);

    // Collect into a default_vec
    let default_vec: Vec<_> = numbers.iter().map(|&x| (x, x * 2)).collect();
    println!("Collected into default_vec: {:?}", default_vec);
}
