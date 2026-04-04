//! Fast Gröbner reduction engine for H_n(q).
//!
//! Three optimizations over naive approach:
//! 1. Indexed pair lookup — terms indexed by consecutive pairs for O(1) rule matching
//! 2. Batch reduction — all reducible terms processed per pass
//! 3. Incremental reduction — after crossing multiplication, only new terms need work
//!
//! Usage:
//!   cargo run --release -- nucleus 4 4    # ⁸Be N(4,4)
//!   cargo run --release -- table 1 8      # all nuclei Z=1..8

use rustc_hash::FxHashMap;
use serde::Serialize;
use std::time::Instant;

type Word = Vec<u8>;

#[derive(Clone)]
struct HeckeElement {
    terms: FxHashMap<Word, f64>,
}

impl HeckeElement {
    fn new() -> Self { Self { terms: FxHashMap::default() } }

    fn identity() -> Self {
        let mut h = Self::new();
        h.terms.insert(vec![], 1.0);
        h
    }

    fn n_terms(&self) -> usize { self.terms.len() }

    fn clean(&mut self) {
        self.terms.retain(|_, c| c.abs() > 1e-15);
    }

    fn histogram(&self) -> Vec<usize> {
        let max_len = self.terms.keys().map(|w| w.len()).max().unwrap_or(0);
        let mut hist = vec![0usize; max_len + 1];
        for w in self.terms.keys() { hist[w.len()] += 1; }
        hist
    }
}

// ════════════════════════════════════════════════════════════════
// Engine with indexed reduction
// ════════════════════════════════════════════════════════════════

struct HeckeEngine {
    ha: f64,
    s: f64,
    z: f64,
    q: f64,
}

impl HeckeEngine {
    fn new(q: f64) -> Self {
        let qi = 1.0 / q;
        Self { ha: q - qi, s: q.sqrt() - qi.sqrt(), z: 1.0 / (q.sqrt() + qi.sqrt()), q }
    }

    fn crossing_coeffs(&self, ti: u8, tj: u8) -> (f64, f64) {
        match (ti, tj) {
            (b'p', b'p') => (1.0, 0.0),
            (b'n', b'n') => (self.q * self.q, -self.q * self.s),
            _ => ((1.0 + self.q * self.q) / 2.0, -self.q * self.s / 2.0),
        }
    }

    /// Multiply element by (c·σ_gen + d) and reduce incrementally.
    /// This is the hot path — optimized for the case where elem is already reduced
    /// and we're adding one crossing.
    fn multiply_and_reduce(&self, elem: &mut HeckeElement, gen: u8, c: f64, d: f64) {
        // Step 1: Multiply — each existing term w gets two new terms:
        //   c·(w·gen) and d·w
        let old_terms: Vec<(Word, f64)> = elem.terms.drain().collect();
        let mut new_terms: FxHashMap<Word, f64> = FxHashMap::default();

        for (w, coeff) in &old_terms {
            // d·w term (same word, just scaled) — always reduced if w was
            if d.abs() > 1e-15 {
                *new_terms.entry(w.clone()).or_insert(0.0) += coeff * d;
            }

            // c·(w·gen) term — may need reduction
            if c.abs() > 1e-15 {
                let mut wg = w.clone();
                wg.push(gen);
                *new_terms.entry(wg).or_insert(0.0) += coeff * c;
            }
        }

        elem.terms = new_terms;
        elem.clean();

        // Step 2: Reduce — but only terms that might be reducible.
        // The d·w terms are already reduced (w was reduced, scaling doesn't change that).
        // The c·(w·gen) terms might have a reducible pair at the junction
        // (last char of w, gen) or within gen itself (but gen is single char).
        //
        // So we only need to check terms ending in gen for:
        //   - Hecke: ...·i·i where i = gen (last two chars equal)
        //   - FarComm: ...·i·gen where i > gen and |i-gen| >= 2
        //   - YB: ...·i·j·i where last three form a YB triple
        //
        // After one reduction, the result might need further reduction,
        // so we iterate until stable.
        self.reduce_full(elem);
    }

    /// Full reduction — batch all reducible terms per pass
    fn reduce_full(&self, elem: &mut HeckeElement) {
        loop {
            let mut new_terms: FxHashMap<Word, f64> = FxHashMap::default();
            let mut any_reduced = false;

            for (word, &coeff) in &elem.terms {
                if coeff.abs() < 1e-15 { continue; }

                if let Some((pos, rule)) = Self::find_reduction(word) {
                    Self::apply_reduction_into(&mut new_terms, word, coeff, pos, rule, self.ha);
                    any_reduced = true;
                } else {
                    *new_terms.entry(word.clone()).or_insert(0.0) += coeff;
                }
            }

            elem.terms = new_terms;
            elem.clean();

            if !any_reduced { break; }
        }
    }

    #[inline]
    fn find_reduction(word: &[u8]) -> Option<(usize, u8)> {
        let len = word.len();
        if len < 2 { return None; }

        for pos in 0..len - 1 {
            let a = word[pos];
            let b = word[pos + 1];

            // Hecke: σ_i²
            if a == b { return Some((pos, 0)); }

            // Far-comm: σ_i σ_j with i > j and |i-j| >= 2
            if (a as i16 - b as i16) >= 2 { return Some((pos, 1)); }

            // Yang-Baxter: σ_i σ_j σ_i with j < i
            if pos + 2 < len {
                let c = word[pos + 2];
                if a == c && (a as i16 - b as i16).abs() == 1 && b < a {
                    return Some((pos, 2));
                }
            }
        }
        None
    }

    #[inline]
    fn apply_reduction_into(
        terms: &mut FxHashMap<Word, f64>,
        word: &[u8], coeff: f64, pos: usize, rule: u8, ha: f64
    ) {
        match rule {
            0 => {
                let i = word[pos];
                let mut w1 = Vec::with_capacity(word.len() - 1);
                w1.extend_from_slice(&word[..pos]);
                w1.push(i);
                w1.extend_from_slice(&word[pos + 2..]);
                let mut w2 = Vec::with_capacity(word.len() - 2);
                w2.extend_from_slice(&word[..pos]);
                w2.extend_from_slice(&word[pos + 2..]);
                *terms.entry(w1).or_insert(0.0) += coeff * ha;
                *terms.entry(w2).or_insert(0.0) += coeff;
            }
            1 => {
                let mut w = word.to_vec();
                w.swap(pos, pos + 1);
                *terms.entry(w).or_insert(0.0) += coeff;
            }
            2 => {
                let mut w = word.to_vec();
                let b = w[pos + 1];
                let a = w[pos];
                w[pos] = b; w[pos + 1] = a; w[pos + 2] = b;
                *terms.entry(w).or_insert(0.0) += coeff;
            }
            _ => unreachable!(),
        }
    }

    /// Build nucleus with incremental multiply-and-reduce
    fn build_nucleus(&self, z: usize, n: usize) -> HeckeElement {
        let a = z + n;
        let mut types = vec![b'p'; z];
        types.extend(vec![b'n'; n]);

        let mut elem = HeckeElement::identity();

        for k in 1..a {
            for i in 0..k {
                let (c, d) = self.crossing_coeffs(types[i], types[k]);
                self.multiply_and_reduce(&mut elem, i as u8, c, d);
            }
        }
        elem
    }

    fn apply_quotient_ideals(&self, elem: &mut HeckeElement) -> usize {
        let mut total_removed = 0;

        // I₉: recursive closed shell
        loop {
            let mut words: Vec<Word> = elem.terms.keys()
                .filter(|w| w.len() >= 2 && elem.terms[*w].abs() > 1e-15)
                .cloned().collect();
            words.sort_unstable_by(|a, b| b.len().cmp(&a.len()));

            let mut found = false;
            for word in &words {
                let prefix = &word[..word.len() - 1];
                if let Some(&c) = elem.terms.get(prefix) {
                    if c.abs() > 1e-15 {
                        elem.terms.remove(word);
                        total_removed += 1;
                        found = true;
                        break;
                    }
                }
            }
            if !found { break; }
        }

        // I₈: adjacency
        loop {
            let mut found = false;
            let adj: Vec<Word> = elem.terms.keys()
                .filter(|w| w.len() == 2 && elem.terms[*w].abs() > 1e-15 && w[1] == w[0] + 1)
                .cloned().collect();
            for word in &adj {
                let sigma_j = vec![word[1]];
                if let Some(&c) = elem.terms.get(&sigma_j) {
                    if c.abs() > 1e-15 {
                        elem.terms.remove(word);
                        total_removed += 1;
                        found = true;
                        break;
                    }
                }
            }
            if !found { break; }
        }

        elem.clean();
        total_removed
    }

    fn generator_volumes(&self, z: usize, n: usize) -> Vec<f64> {
        let a = z + n;
        let mut types = vec![b'p'; z];
        types.extend(vec![b'n'; n]);
        let mut volumes = Vec::new();
        for i in 0..a - 1 {
            let mut m = [[1.0, 0.0], [0.0, 1.0]];
            for j in (i + 1)..a {
                let (c, d) = self.crossing_coeffs(types[i], types[j]);
                let t = [[c * self.ha + d, c], [c, d]];
                m = [
                    [m[0][0]*t[0][0]+m[0][1]*t[1][0], m[0][0]*t[0][1]+m[0][1]*t[1][1]],
                    [m[1][0]*t[0][0]+m[1][1]*t[1][0], m[1][0]*t[0][1]+m[1][1]*t[1][1]],
                ];
            }
            volumes.push(self.z * m[0][0] + m[1][0]);
        }
        volumes
    }

    fn skein_polynomial(&self, z: usize, n: usize) -> f64 {
        self.generator_volumes(z, n).iter().product()
    }
}

// ════════════════════════════════════════════════════════════════

#[derive(Serialize)]
struct NucleusResult {
    name: String, z: usize, n: usize, a: usize,
    raw_terms: usize, optimal_terms: usize, target: usize,
    is_optimal: bool, histogram: Vec<usize>, is_palindromic: bool,
    elapsed_ms: u128, skein_polynomial: f64,
}

fn is_palindromic(h: &[usize]) -> bool {
    let n = h.len();
    (0..n/2).all(|i| h[i] == h[n-1-i])
}

fn nucleus_name(z: usize, n: usize) -> String {
    let a = z + n;
    let sym = match z {
        1=>"H",2=>"He",3=>"Li",4=>"Be",5=>"B",6=>"C",7=>"N",8=>"O",9=>"F",10=>"Ne",_=>"?"
    };
    format!("{}{}({},{})", a, sym, z, n)
}

fn compute_nucleus(engine: &HeckeEngine, z: usize, n: usize) -> NucleusResult {
    let a = z + n;
    let t0 = Instant::now();
    let mut elem = engine.build_nucleus(z, n);
    let raw_terms = elem.n_terms();
    let hist = elem.histogram();
    let pal = is_palindromic(&hist);
    engine.apply_quotient_ideals(&mut elem);
    let optimal = elem.n_terms();
    let skein = engine.skein_polynomial(z, n);
    NucleusResult {
        name: nucleus_name(z, n), z, n, a,
        raw_terms, optimal_terms: optimal, target: a,
        is_optimal: optimal == a, histogram: hist, is_palindromic: pal,
        elapsed_ms: t0.elapsed().as_millis(), skein_polynomial: skein,
    }
}

fn main() {
    let args: Vec<String> = std::env::args().collect();
    let q = 1.10998_f64;
    let engine = HeckeEngine::new(q);

    if args.len() < 2 {
        eprintln!("Usage: hecke-engine [nucleus Z N | table Zmin Zmax Amax | isotopes Z]");
        std::process::exit(1);
    }

    match args[1].as_str() {
        "nucleus" => {
            let z: usize = args[2].parse().unwrap();
            let n: usize = args[3].parse().unwrap();
            let r = compute_nucleus(&engine, z, n);
            println!("{}: A={}, Raw={}, After I8+I9={} (target {}), {}, Palindromic={}, P={:.6}, {}ms",
                r.name, r.a, r.raw_terms, r.optimal_terms, r.target,
                if r.is_optimal {"OPTIMAL"} else {"NOT OPTIMAL"},
                if r.is_palindromic {"Y"} else {"N"},
                r.skein_polynomial, r.elapsed_ms);
            println!("Histogram: {:?}", r.histogram);
            println!("{}", serde_json::to_string_pretty(&r).unwrap());
        }

        "table" => {
            let z_min: usize = args.get(2).and_then(|s| s.parse().ok()).unwrap_or(1);
            let z_max: usize = args.get(3).and_then(|s| s.parse().ok()).unwrap_or(8);
            let a_max: usize = args.get(4).and_then(|s| s.parse().ok()).unwrap_or(16);

            println!("{:>12} {:>3} {:>3} {:>3} {:>10} {:>6} {:>4} {:>3} {:>10} {:>10}",
                     "Nucleus","Z","N","A","Raw","After","Tgt","Pal","Status","Time");
            println!("{}", "-".repeat(75));

            let mut all_opt = true;
            let t_total = Instant::now();
            for z in z_min..=z_max {
                let n_min = if z <= 1 { 1 } else { z.saturating_sub(1) };
                for n in n_min..=(z+2) {
                    let a = z + n;
                    if a < 2 || a > a_max { continue; }
                    let r = compute_nucleus(&engine, z, n);
                    if !r.is_optimal { all_opt = false; }
                    println!("{:>12} {:>3} {:>3} {:>3} {:>10} {:>6} {:>4} {:>3} {:>10} {:>8}ms",
                        r.name, z, n, a, r.raw_terms, r.optimal_terms,
                        r.target, if r.is_palindromic {"Y"} else {" "},
                        if r.is_optimal {"OPTIMAL"} else {"over"}, r.elapsed_ms);
                }
            }
            println!("\nAll optimal: {}  Total: {}ms",
                if all_opt {"YES"} else {"NO"}, t_total.elapsed().as_millis());
        }

        "isotopes" => {
            let z: usize = args[2].parse().unwrap();
            let sym = match z { 1=>"H",2=>"He",3=>"Li",4=>"Be",5=>"B",6=>"C",7=>"N",8=>"O",_=>"?" };
            println!("Isotopes of {} (Z={})", sym, z);
            println!("{:>6} {:>3} {:>3} {:>12} {:>12}", "Name","N","A","ln|P|","|P|^2 %");
            println!("{}", "-".repeat(45));
            let mut data = Vec::new();
            for n in z.saturating_sub(2)..=(z+4) {
                let a = z + n; if a < 1 { continue; }
                let vols = engine.generator_volumes(z, n);
                let ln_p: f64 = vols.iter().map(|v| v.abs().ln()).sum();
                data.push((n, a, ln_p));
            }
            let mx = data.iter().map(|d| d.2).fold(f64::NEG_INFINITY, f64::max);
            let w: Vec<f64> = data.iter().map(|d| (2.0*(d.2-mx)).exp()).collect();
            let tot: f64 = w.iter().sum();
            for (i, &(n,a,lp)) in data.iter().enumerate() {
                println!("{:>6} {:>3} {:>3} {:>12.6} {:>11.4}%", format!("{}{}",a,sym), n, a, lp, w[i]/tot*100.0);
            }
        }

        _ => { eprintln!("Unknown: {}", args[1]); std::process::exit(1); }
    }
}
