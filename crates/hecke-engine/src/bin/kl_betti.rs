use hecke_engine::kazhdan_lusztig::{KLContext, Perm};
use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();
    let n: usize = if args.len() > 1 { args[1].parse().unwrap() } else { 6 };
    println!("Initializing Kazhdan-Lusztig for S_{}...", n);
    let mut ctx = KLContext::new(n);
    let identity = Perm::identity(n);
    println!("Context initialized with {} permutations.", (1..=n).product::<usize>());
    
    // Example: Evaluate for longest element to test
    let mut w_elements = Vec::with_capacity(n);
    for i in 0..n {
        w_elements.push((n - i) as u8);
    }
    let w0 = Perm::new(n, &w_elements);
    
    println!("Testing P_{{e, w_0}}...");
    let p = ctx.kl_polynomial(identity, w0);
    println!("P_{{e, w_0}} = {:?}", p.coeffs);
    println!("Betti sum = {}", p.eval_at_1());
}
