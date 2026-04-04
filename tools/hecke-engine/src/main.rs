//! Fast Gröbner reduction engine for H_n(q).
//!
//! Computes nuclear normal forms with quotient ideals I₈ (adjacency)
//! and I₉ (closed shell). Uses f64 arithmetic for speed.
//!
//! Usage:
//!   cargo run --release -- nucleus 4 4    # ⁸Be N(4,4)
//!   cargo run --release -- table 1 8      # all nuclei Z=1..8
//!   cargo run --release -- isotopes 2     # He isotopes

use rustc_hash::FxHashMap;
use serde::Serialize;
use std::time::Instant;

// ════════════════════════════════════════════════════════════════
// Hecke algebra element: HashMap<Word, f64>
// Word = Vec<u8> (generator indices, max 255 generators)
// ════════════════════════════════════════════════════════════════

type Word = Vec<u8>;

#[derive(Clone)]
struct HeckeElement {
    terms: FxHashMap<Word, f64>,
}

impl HeckeElement {
    fn new() -> Self {
        Self { terms: FxHashMap::default() }
    }

    fn identity() -> Self {
        let mut h = Self::new();
        h.terms.insert(vec![], 1.0);
        h
    }

    fn from_single(word: Word, coeff: f64) -> Self {
        let mut h = Self::new();
        if coeff.abs() > 1e-15 {
            h.terms.insert(word, coeff);
        }
        h
    }

    fn from_two(w1: Word, c1: f64, w2: Word, c2: f64) -> Self {
        let mut h = Self::new();
        if c1.abs() > 1e-15 { h.terms.insert(w1, c1); }
        if c2.abs() > 1e-15 { h.terms.insert(w2, c2); }
        h
    }

    fn n_terms(&self) -> usize {
        self.terms.len()
    }

    fn clean(&mut self) {
        self.terms.retain(|_, c| c.abs() > 1e-15);
    }

    fn multiply(&self, other: &HeckeElement) -> HeckeElement {
        let mut result = HeckeElement::new();
        for (w1, c1) in &self.terms {
            for (w2, c2) in &other.terms {
                let mut w = w1.clone();
                w.extend_from_slice(w2);
                *result.terms.entry(w).or_insert(0.0) += c1 * c2;
            }
        }
        result.clean();
        result
    }

    fn histogram(&self) -> Vec<usize> {
        let max_len = self.terms.keys().map(|w| w.len()).max().unwrap_or(0);
        let mut hist = vec![0usize; max_len + 1];
        for w in self.terms.keys() {
            hist[w.len()] += 1;
        }
        hist
    }
}

// ════════════════════════════════════════════════════════════════
// Gröbner reduction engine
// ════════════════════════════════════════════════════════════════

struct HeckeEngine {
    ha: f64,     // q - q⁻¹
    s: f64,      // q^½ - q^{-½}
    z: f64,      // 1/(q^½ + q^{-½})
    q: f64,
}

impl HeckeEngine {
    fn new(q: f64) -> Self {
        let qi = 1.0 / q;
        Self {
            ha: q - qi,
            s: q.sqrt() - qi.sqrt(),
            z: 1.0 / (q.sqrt() + qi.sqrt()),
            q,
        }
    }

    /// Crossing coefficients (c, d) for nucleon pair types
    fn crossing_coeffs(&self, ti: u8, tj: u8) -> (f64, f64) {
        match (ti, tj) {
            (b'p', b'p') => (1.0, 0.0),
            (b'n', b'n') => (self.q * self.q, -self.q * self.s),
            _ => ((1.0 + self.q * self.q) / 2.0, -self.q * self.s / 2.0),
        }
    }

    /// Build crossing element: c·σ_gen + d·𝟏
    fn crossing(&self, ti: u8, tj: u8, gen: u8) -> HeckeElement {
        let (c, d) = self.crossing_coeffs(ti, tj);
        HeckeElement::from_two(vec![gen], c, vec![], d)
    }

    /// Gröbner reduction: apply Hecke, far-comm, YB rules until convergence
    fn reduce(&self, elem: &mut HeckeElement) {
        let mut changed = true;
        let mut iterations = 0;
        while changed && iterations < 100_000 {
            changed = false;
            let mut new_terms: FxHashMap<Word, f64> = FxHashMap::default();

            for (word, &coeff) in &elem.terms {
                if coeff.abs() < 1e-15 { continue; }
                let mut reduced = false;

                // Rule 1: Hecke — σ_i² → (q-q⁻¹)σ_i + 1
                for pos in 0..word.len().saturating_sub(1) {
                    if word[pos] == word[pos + 1] {
                        let i = word[pos];
                        let mut w1: Vec<u8> = word[..pos].to_vec();
                        w1.push(i);
                        w1.extend_from_slice(&word[pos + 2..]);

                        let mut w2: Vec<u8> = word[..pos].to_vec();
                        w2.extend_from_slice(&word[pos + 2..]);

                        *new_terms.entry(w1).or_insert(0.0) += coeff * self.ha;
                        *new_terms.entry(w2).or_insert(0.0) += coeff;
                        reduced = true;
                        changed = true;
                        break;
                    }
                }
                if reduced { continue; }

                // Rule 2: Far-commutativity — σ_iσ_j → σ_jσ_i for |i-j| ≥ 2
                for pos in 0..word.len().saturating_sub(1) {
                    let (a, b) = (word[pos], word[pos + 1]);
                    if a > b && (a as i16 - b as i16).unsigned_abs() >= 2 {
                        let mut w = word.clone();
                        w[pos] = b;
                        w[pos + 1] = a;
                        *new_terms.entry(w).or_insert(0.0) += coeff;
                        reduced = true;
                        changed = true;
                        break;
                    }
                }
                if reduced { continue; }

                // Rule 3: Yang-Baxter — σ_iσ_{i+1}σ_i → σ_{i+1}σ_iσ_{i+1}
                for pos in 0..word.len().saturating_sub(2) {
                    let (a, b, c) = (word[pos], word[pos + 1], word[pos + 2]);
                    if a == c && (a as i16 - b as i16).abs() == 1 {
                        let new_trip = if b < a { (b, a, b) } else { continue };
                        // Only apply if replacement is lex-smaller
                        if (new_trip.0, new_trip.1, new_trip.2) < (a, b, c) {
                            let mut w = word.clone();
                            w[pos] = new_trip.0;
                            w[pos + 1] = new_trip.1;
                            w[pos + 2] = new_trip.2;
                            *new_terms.entry(w).or_insert(0.0) += coeff;
                            reduced = true;
                            changed = true;
                            break;
                        }
                    }
                }

                if !reduced {
                    *new_terms.entry(word.clone()).or_insert(0.0) += coeff;
                }
            }

            elem.terms = new_terms;
            elem.clean();
            iterations += 1;
        }
    }

    /// Build nucleus N(Z, N) inductively with reduction at each step
    fn build_nucleus(&self, z: usize, n: usize) -> HeckeElement {
        let a = z + n;
        let mut types = vec![b'p'; z];
        types.extend(vec![b'n'; n]);

        let mut elem = HeckeElement::identity();

        for k in 1..a {
            for i in 0..k {
                let cx = self.crossing(types[i], types[k], i as u8);
                elem = elem.multiply(&cx);
                self.reduce(&mut elem);
            }
        }
        elem
    }

    /// Apply I₈ (adjacency) + I₉ (closed shell) quotient ideals
    fn apply_quotient_ideals(&self, elem: &mut HeckeElement) -> usize {
        let mut total_removed = 0;

        // I₉ first (recursive closed shell): strip longest chains
        loop {
            let mut words: Vec<Word> = elem.terms.keys()
                .filter(|w| w.len() >= 2 && elem.terms[*w].abs() > 1e-15)
                .cloned()
                .collect();
            words.sort_by(|a, b| b.len().cmp(&a.len()));

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

        // I₈ (adjacency): absorb σ_i·σ_{i+1}
        loop {
            let mut found = false;
            let words: Vec<(Word, f64)> = elem.terms.iter()
                .filter(|(w, c)| w.len() == 2 && c.abs() > 1e-15)
                .map(|(w, &c)| (w.clone(), c))
                .collect();

            for (word, _coeff) in &words {
                let (i, j) = (word[0], word[1]);
                if j == i + 1 {
                    let sigma_j = vec![j];
                    if let Some(&c_j) = elem.terms.get(&sigma_j) {
                        if c_j.abs() > 1e-15 {
                            elem.terms.remove(&word.clone());
                            total_removed += 1;
                            found = true;
                            break;
                        }
                    }
                }
            }
            if !found { break; }
        }

        elem.clean();
        total_removed
    }

    /// Compute per-generator Markov-traced volumes (transfer matrix method)
    fn generator_volumes(&self, z: usize, n: usize) -> Vec<f64> {
        let a = z + n;
        let mut types = vec![b'p'; z];
        types.extend(vec![b'n'; n]);
        let mut volumes = Vec::new();

        for i in 0..a - 1 {
            // M_i = product of T(c,d) for j > i
            let mut m = [[1.0, 0.0], [0.0, 1.0]]; // identity
            for j in (i + 1)..a {
                let (c, d) = self.crossing_coeffs(types[i], types[j]);
                let t = [[c * self.ha + d, c], [c, d]];
                let new_m = [
                    [m[0][0]*t[0][0] + m[0][1]*t[1][0], m[0][0]*t[0][1] + m[0][1]*t[1][1]],
                    [m[1][0]*t[0][0] + m[1][1]*t[1][0], m[1][0]*t[0][1] + m[1][1]*t[1][1]],
                ];
                m = new_m;
            }
            volumes.push(self.z * m[0][0] + m[1][0]);
        }
        volumes
    }

    /// Skein polynomial P = ∏ V̂_i
    fn skein_polynomial(&self, z: usize, n: usize) -> f64 {
        self.generator_volumes(z, n).iter().product()
    }
}

// ════════════════════════════════════════════════════════════════
// Output structures
// ════════════════════════════════════════════════════════════════

#[derive(Serialize)]
struct NucleusResult {
    name: String,
    z: usize,
    n: usize,
    a: usize,
    raw_terms: usize,
    optimal_terms: usize,
    target: usize,
    is_optimal: bool,
    histogram: Vec<usize>,
    is_palindromic: bool,
    elapsed_ms: u128,
    skein_polynomial: f64,
}

fn is_palindromic(hist: &[usize]) -> bool {
    let n = hist.len();
    for i in 0..n / 2 {
        if hist[i] != hist[n - 1 - i] { return false; }
    }
    true
}

fn nucleus_name(z: usize, n: usize) -> String {
    let a = z + n;
    let sym = match z {
        1 => "H", 2 => "He", 3 => "Li", 4 => "Be", 5 => "B",
        6 => "C", 7 => "N", 8 => "O", 9 => "F", 10 => "Ne",
        _ => "?",
    };
    format!("{}{}({}{})", a, sym, z, if n > 0 { format!(",{}", n) } else { String::new() })
}

// ════════════════════════════════════════════════════════════════
// Main
// ════════════════════════════════════════════════════════════════

fn compute_nucleus(engine: &HeckeEngine, z: usize, n: usize) -> NucleusResult {
    let a = z + n;
    let t0 = Instant::now();

    let mut elem = engine.build_nucleus(z, n);
    let raw_terms = elem.n_terms();
    let hist = elem.histogram();
    let palindromic = is_palindromic(&hist);

    engine.apply_quotient_ideals(&mut elem);
    let optimal_terms = elem.n_terms();

    let skein = engine.skein_polynomial(z, n);

    NucleusResult {
        name: nucleus_name(z, n),
        z, n, a,
        raw_terms,
        optimal_terms,
        target: a,
        is_optimal: optimal_terms == a,
        histogram: hist,
        is_palindromic: palindromic,
        elapsed_ms: t0.elapsed().as_millis(),
        skein_polynomial: skein,
    }
}

fn main() {
    let args: Vec<String> = std::env::args().collect();
    let q = 1.10998_f64;
    let engine = HeckeEngine::new(q);

    if args.len() < 2 {
        eprintln!("Usage:");
        eprintln!("  hecke-engine nucleus Z N     # compute single nucleus");
        eprintln!("  hecke-engine table Z_min Z_max  # table of nuclei");
        eprintln!("  hecke-engine isotopes Z      # isotopes of element Z");
        std::process::exit(1);
    }

    match args[1].as_str() {
        "nucleus" => {
            let z: usize = args[2].parse().unwrap();
            let n: usize = args[3].parse().unwrap();
            let result = compute_nucleus(&engine, z, n);

            println!("{}:", result.name);
            println!("  A = {}, Z = {}, N = {}", result.a, z, n);
            println!("  Raw terms: {}", result.raw_terms);
            println!("  Histogram: {:?}", result.histogram);
            println!("  Palindromic: {}", if result.is_palindromic { "★ YES" } else { "NO" });
            println!("  After I₈+I₉: {} terms (target {})", result.optimal_terms, result.target);
            println!("  Status: {}", if result.is_optimal { "OPTIMAL ★" } else { "NOT OPTIMAL" });
            println!("  P(q₀) = {:.10}", result.skein_polynomial);
            println!("  Time: {}ms", result.elapsed_ms);

            // JSON output
            let json = serde_json::to_string_pretty(&result).unwrap();
            println!("\n{}", json);
        }

        "table" => {
            let z_min: usize = args.get(2).and_then(|s| s.parse().ok()).unwrap_or(1);
            let z_max: usize = args.get(3).and_then(|s| s.parse().ok()).unwrap_or(8);

            println!("{:>12} {:>3} {:>3} {:>3} {:>8} {:>8} {:>4} {:>3} {:>12} {:>8}",
                     "Nucleus", "Z", "N", "A", "Raw", "After", "Tgt", "Pal", "Status", "Time");
            println!("{}", "-".repeat(80));

            let mut results = Vec::new();
            for z in z_min..=z_max {
                // Stable-ish isotopes: N from max(1, z-1) to z+2
                let n_min = if z <= 1 { 1 } else { z.saturating_sub(1) };
                let n_max = z + 2;
                for n in n_min..=n_max {
                    let a = z + n;
                    if a < 2 || a > 16 { continue; } // cap at A=16 for speed

                    let r = compute_nucleus(&engine, z, n);
                    let status = if r.is_optimal { "OPTIMAL ★" } else { "over" };
                    let pal = if r.is_palindromic { "★" } else { " " };
                    println!("{:>12} {:>3} {:>3} {:>3} {:>8} {:>8} {:>4} {:>3} {:>12} {:>6}ms",
                             r.name, z, n, a, r.raw_terms, r.optimal_terms,
                             r.target, pal, status, r.elapsed_ms);
                    results.push(r);
                }
            }

            // Summary
            let all_optimal = results.iter().all(|r| r.is_optimal);
            let all_palindromic = results.iter().all(|r| r.is_palindromic);
            println!();
            println!("All optimal: {}", if all_optimal { "★ YES" } else { "NO" });
            println!("All palindromic: {}", if all_palindromic { "★ YES" } else { "NO" });
        }

        "isotopes" => {
            let z: usize = args[2].parse().unwrap();
            let sym = match z {
                1 => "H", 2 => "He", 3 => "Li", 4 => "Be", 5 => "B",
                6 => "C", 7 => "N", 8 => "O", _ => "?",
            };
            println!("Isotopes of {} (Z={})", sym, z);
            println!("{:>6} {:>3} {:>3} {:>12} {:>12}", "Name", "N", "A", "ln|P|", "|P|²");
            println!("{}", "-".repeat(45));

            let mut ln_ps = Vec::new();
            let n_min = if z <= 1 { 0 } else { z.saturating_sub(2) };
            let n_max = z + 4;

            for n in n_min..=n_max {
                let a = z + n;
                if a < 1 { continue; }
                let vols = engine.generator_volumes(z, n);
                let mut ln_p = 0.0;
                for &v in &vols {
                    if v.abs() > 1e-30 {
                        ln_p += v.abs().ln();
                    }
                }
                ln_ps.push((n, a, ln_p));
            }

            // Normalize |P|² abundances
            let max_ln = ln_ps.iter().map(|&(_, _, lp)| lp).fold(f64::NEG_INFINITY, f64::max);
            let weights: Vec<f64> = ln_ps.iter()
                .map(|&(_, _, lp)| (2.0 * (lp - max_ln)).exp())
                .collect();
            let total: f64 = weights.iter().sum();

            for (idx, &(n, a, ln_p)) in ln_ps.iter().enumerate() {
                let pct = weights[idx] / total * 100.0;
                let name = format!("{}{}", a, sym);
                println!("{:>6} {:>3} {:>3} {:>12.6} {:>11.4}%", name, n, a, ln_p, pct);
            }
        }

        _ => {
            eprintln!("Unknown command: {}", args[1]);
            std::process::exit(1);
        }
    }
}
