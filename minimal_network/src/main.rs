use std::f32::INFINITY;
use std::fs::File;
use std::io::prelude::*;
use std::path::Path;

fn find_min(adj: Vec<Vec<i32>>, lst_opened: Vec<usize>) -> (i32, i32) {
    let min_paths = INFINITY;
    for opened in lst_opened.iter() {
        let line = adj.get(*opened).unwrap();
        let min_path = line.iter().min().unwrap();
        let node_index = line.iter().position(|&w| w == *min_path).unwrap();
    }
    (0, 0)
}

fn main() {
    // Create a path to the desired file
    let path = Path::new("resources/p107_network.txt");
    let display = path.display();

    // Open the path in read-only mode, returns `io::Result<File>`
    let mut file = match File::open(&path) {
        Err(why) => panic!("couldn't open {}: {}", display, why),
        Ok(file) => file,
    };

    // Read the file contents into a string, returns `io::Result<usize>`
    let mut s = String::new();
    match file.read_to_string(&mut s) {
        Err(why) => panic!("couldn't read {}: {}", display, why),
        Ok(_) => print!("{} contains:\n{}", display, s),
    }
    // let content: Vec<Vec<String>> = s
    //     .split('\n')
    //     .map(|line| {
    //         // println!("{}", line);
    //         line.split(',').map(|value| {
    //             print!("{}", value);
    //             match value {
    //                 "-" => INFINITY,
    //                 a => a.parse().unwrap(),
    //             }
    //         })
    //     })
    //     .collect();
    // println!("{}", content);

    // `file` goes out of scope, and the "hello.txt" file gets closed
}
