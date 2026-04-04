//! Fast Gröbner reduction engine for H_n(q).
//!
//! Monomial ordering: degree-reverse-lex (degrevlex).
//!   1. Degree (word length) — Hecke reduces high → low
//!   2. Reverse-lex — within same degree, larger rightmost generator first
//!
//! Key optimization: separate reduced/unreduced term pools.
//! Never scan reduced terms — only process the unreduced queue.
//!
//! Usage:
//!   cargo run --release -- nucleus Z N
//!   cargo run --release -- table Zmin Zmax [Amax]

use rustc_hash::FxHashMap;
use serde::Serialize;
use std::collections::BinaryHeap;
use std::cmp::Ordering;
use std::time::Instant;

type Word = Vec<u8>;

/// Priority wrapper: highest word length first (max-heap by degree)
#[derive(Clone)]
struct PriWord(Word, f64);

impl PartialEq for PriWord {
    fn eq(&self, other: &Self) -> bool { self.0.len() == other.0.len() }
}
impl Eq for PriWord {}
impl PartialOrd for PriWord {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> { Some(self.cmp(other)) }
}
impl Ord for PriWord {
    fn cmp(&self, other: &Self) -> Ordering {
        self.0.len().cmp(&other.0.len()) // highest degree first
    }
}

// ════════════════════════════════════════════════════════════════
// Hecke element with reduced/unreduced separation
// ════════════════════════════════════════════════════════════════

struct HeckeElement {
    /// Fully reduced terms
    reduced: FxHashMap<Word, f64>,
    /// Priority queue: highest degree terms processed first.
    /// Hecke reductions produce lower-degree output, so processing
    /// top-down means each degree level is visited at most once.
    unreduced: BinaryHeap<PriWord>,
}

impl HeckeElement {
    fn new() -> Self {
        Self { reduced: FxHashMap::default(), unreduced: BinaryHeap::new() }
    }

    fn identity() -> Self {
        let mut h = Self::new();
        h.reduced.insert(vec![], 1.0);
        h
    }

    fn n_terms(&self) -> usize { self.reduced.len() }

    fn into_map(self) -> FxHashMap<Word, f64> { self.reduced }

    fn histogram(&self) -> Vec<usize> {
        let max_len = self.reduced.keys().map(|w| w.len()).max().unwrap_or(0);
        let mut hist = vec![0usize; max_len + 1];
        for w in self.reduced.keys() { hist[w.len()] += 1; }
        hist
    }
}

// ════════════════════════════════════════════════════════════════
// Engine
// ════════════════════════════════════════════════════════════════

struct HeckeEngine {
    ha: f64, s: f64, z: f64, q: f64,
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

    /// Check if word is reducible. Returns first reducible site.
    #[inline]
    fn find_reduction(word: &[u8]) -> Option<(usize, u8)> {
        let len = word.len();
        if len < 2 { return None; }
        for pos in 0..len - 1 {
            let a = word[pos];
            let b = word[pos + 1];
            if a == b { return Some((pos, 0)); }                    // Hecke
            if (a as i16 - b as i16) >= 2 { return Some((pos, 1)); } // FC
            if pos + 2 < len {
                let c = word[pos + 2];
                if a == c && (a as i16 - b as i16).abs() == 1 && b < a {
                    return Some((pos, 2));                           // YB
                }
            }
        }
        None
    }

    /// Add a term, routing to reduced or unreduced (priority queue).
    #[inline]
    fn add_term(elem: &mut HeckeElement, word: Word, coeff: f64) {
        if coeff.abs() < 1e-15 { return; }
        if Self::find_reduction(&word).is_some() {
            elem.unreduced.push(PriWord(word, coeff));
        } else {
            *elem.reduced.entry(word).or_insert(0.0) += coeff;
        }
    }

    /// Process unreduced terms highest-degree-first until empty.
    /// Consolidates same-word entries before processing to avoid
    /// redundant reductions.
    fn drain_unreduced(&self, elem: &mut HeckeElement) {
        // Consolidation: drain heap into a map grouped by word,
        // then process each unique word once.
        while !elem.unreduced.is_empty() {
            // Drain current batch into consolidation map
            let mut batch: FxHashMap<Word, f64> = FxHashMap::default();
            while let Some(PriWord(word, coeff)) = elem.unreduced.pop() {
                *batch.entry(word).or_insert(0.0) += coeff;
            }

            // Process consolidated batch
            for (word, coeff) in batch {
            if coeff.abs() < 1e-15 { continue; }

            if let Some((pos, rule)) = Self::find_reduction(&word) {
                match rule {
                    0 => {
                        // Hecke: σ_i² → ha·σ_i + 1
                        let i = word[pos];
                        let mut w1 = Vec::with_capacity(word.len() - 1);
                        w1.extend_from_slice(&word[..pos]);
                        w1.push(i);
                        w1.extend_from_slice(&word[pos + 2..]);

                        let mut w2 = Vec::with_capacity(word.len() - 2);
                        w2.extend_from_slice(&word[..pos]);
                        w2.extend_from_slice(&word[pos + 2..]);

                        Self::add_term(elem, w1, coeff * self.ha);
                        Self::add_term(elem, w2, coeff);
                    }
                    1 => {
                        // Far-comm: swap
                        let mut w = word;
                        w.swap(pos, pos + 1);
                        Self::add_term(elem, w, coeff);
                    }
                    2 => {
                        // YB: (a,b,a) → (b,a,b)
                        let mut w = word;
                        let a = w[pos]; let b = w[pos+1];
                        w[pos] = b; w[pos+1] = a; w[pos+2] = b;
                        Self::add_term(elem, w, coeff);
                    }
                    _ => unreachable!(),
                }
            } else {
                *elem.reduced.entry(word).or_insert(0.0) += coeff;
            }
            } // end for (word, coeff) in batch
        } // end while !unreduced.is_empty()

        elem.reduced.retain(|_, c| c.abs() > 1e-15);
    }

    /// Multiply element by (c·σ_gen + d) and reduce.
    fn multiply_and_reduce(&self, elem: &mut HeckeElement, gen: u8, c: f64, d: f64) {
        // Take all reduced terms, multiply, route results
        let old: Vec<(Word, f64)> = elem.reduced.drain().collect();

        for (w, coeff) in old {
            // d·w — same word, check if still reduced
            if d.abs() > 1e-15 {
                // w was reduced. d·w has same word → still reduced
                *elem.reduced.entry(w.clone()).or_insert(0.0) += coeff * d;
            }

            // c·(w·gen) — appending gen may create a reducible pair
            if c.abs() > 1e-15 {
                let new_coeff = coeff * c;
                // Check: is the last char of w adjacent to gen?
                // If w is empty or last char != gen and far-comm/YB don't apply,
                // then w·gen is reduced.
                let mut wg = w;
                wg.push(gen);
                Self::add_term(elem, wg, new_coeff);
            }
        }

        self.drain_unreduced(elem);
    }

    fn build_nucleus(&self, z: usize, n: usize) -> HeckeElement {
        self.build_nucleus_inner(z, n, false)
    }

    /// Build with quotient ideals applied at each step (keeps terms bounded)
    fn build_nucleus_quotient(&self, z: usize, n: usize) -> HeckeElement {
        self.build_nucleus_inner(z, n, true)
    }

    fn build_nucleus_inner(&self, z: usize, n: usize, use_quotient: bool) -> HeckeElement {
        let a = z + n;
        let mut types = vec![b'p'; z];
        types.extend(vec![b'n'; n]);
        let mut elem = HeckeElement::identity();

        for k in 1..a {
            for i in 0..k {
                let (c, d) = self.crossing_coeffs(types[i], types[k]);
                self.multiply_and_reduce(&mut elem, i as u8, c, d);
            }
            if use_quotient {
                // Apply quotient after completing all crossings for strand k
                let mut terms = std::mem::take(&mut elem.reduced);
                Self::apply_quotient_ideals(&mut terms);
                elem.reduced = terms;
            }
        }
        elem
    }

    fn apply_quotient_ideals(terms: &mut FxHashMap<Word, f64>) -> usize {
        let mut total = 0;
        // I₉: strip longest chains recursively
        loop {
            let mut words: Vec<Word> = terms.keys()
                .filter(|w| w.len() >= 2 && terms[*w].abs() > 1e-15)
                .cloned().collect();
            words.sort_unstable_by(|a, b| b.len().cmp(&a.len()));
            let mut found = false;
            for word in &words {
                let prefix = &word[..word.len()-1];
                if terms.get(prefix).map_or(false, |c| c.abs() > 1e-15) {
                    terms.remove(word);
                    total += 1; found = true; break;
                }
            }
            if !found { break; }
        }
        // I₈: adjacency
        loop {
            let adj: Vec<Word> = terms.keys()
                .filter(|w| w.len() == 2 && terms[*w].abs() > 1e-15 && w[1] == w[0]+1)
                .cloned().collect();
            let mut found = false;
            for word in &adj {
                if terms.get(&vec![word[1]]).map_or(false, |c| c.abs() > 1e-15) {
                    terms.remove(&word.clone()); total += 1; found = true; break;
                }
            }
            if !found { break; }
        }
        terms.retain(|_, c| c.abs() > 1e-15);
        total
    }

    fn generator_volumes(&self, z: usize, n: usize) -> Vec<f64> {
        let a = z + n;
        let mut types = vec![b'p'; z];
        types.extend(vec![b'n'; n]);
        (0..a-1).map(|i| {
            let mut m = [[1.0,0.0],[0.0,1.0]];
            for j in (i+1)..a {
                let (c, d) = self.crossing_coeffs(types[i], types[j]);
                let t = [[c*self.ha+d, c], [c, d]];
                m = [[m[0][0]*t[0][0]+m[0][1]*t[1][0], m[0][0]*t[0][1]+m[0][1]*t[1][1]],
                     [m[1][0]*t[0][0]+m[1][1]*t[1][0], m[1][0]*t[0][1]+m[1][1]*t[1][1]]];
            }
            self.z * m[0][0] + m[1][0]
        }).collect()
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
    let n = h.len(); (0..n/2).all(|i| h[i] == h[n-1-i])
}

fn nucleus_name(z: usize, n: usize) -> String {
    let a = z+n;
    let s = match z {1=>"H",2=>"He",3=>"Li",4=>"Be",5=>"B",6=>"C",7=>"N",8=>"O",_=>"?"};
    format!("{}{}({},{})", a, s, z, n)
}

fn compute(engine: &HeckeEngine, z: usize, n: usize) -> NucleusResult {
    let a = z+n;
    let t0 = Instant::now();

    // Build with quotient ideals at each step for large nuclei
    let (raw, hist, pal, opt) = if a <= 8 {
        // Small: compute full NF first, then apply quotient (to get raw count)
        let elem = engine.build_nucleus(z, n);
        let raw = elem.n_terms();
        let hist = elem.histogram();
        let pal = is_palindromic(&hist);
        let mut terms = elem.into_map();
        HeckeEngine::apply_quotient_ideals(&mut terms);
        (raw, hist, pal, terms.len())
    } else {
        // Large: apply quotient at each step to keep terms bounded
        let elem = engine.build_nucleus_quotient(z, n);
        let opt = elem.n_terms();
        let hist = elem.histogram();
        let pal = is_palindromic(&hist);
        // raw is unknown (we didn't compute the full expansion)
        (0, hist, pal, opt)
    };
    let skein: f64 = engine.generator_volumes(z, n).iter().product();
    NucleusResult {
        name: nucleus_name(z,n), z, n, a, raw_terms: raw,
        optimal_terms: opt, target: a, is_optimal: opt==a,
        histogram: hist, is_palindromic: pal,
        elapsed_ms: t0.elapsed().as_millis(), skein_polynomial: skein,
    }
}

fn main() {
    let args: Vec<String> = std::env::args().collect();
    let engine = HeckeEngine::new(1.10998);

    if args.len() < 2 {
        eprintln!("Usage: hecke-engine [nucleus Z N | table Zmin Zmax [Amax]]");
        std::process::exit(1);
    }

    match args[1].as_str() {
        "nucleus" => {
            let z: usize = args[2].parse().unwrap();
            let n: usize = args[3].parse().unwrap();
            let r = compute(&engine, z, n);
            println!("{}: A={}, Raw={}, Optimal={} (target {}), {}, Pal={}, P={:.6}, {}ms",
                r.name, r.a, r.raw_terms, r.optimal_terms, r.target,
                if r.is_optimal {"OPTIMAL"} else {"NOT OPTIMAL"},
                if r.is_palindromic {"Y"} else {"N"}, r.skein_polynomial, r.elapsed_ms);
            println!("Histogram: {:?}", r.histogram);
        }

        "table" => {
            let z_min: usize = args.get(2).and_then(|s| s.parse().ok()).unwrap_or(1);
            let z_max: usize = args.get(3).and_then(|s| s.parse().ok()).unwrap_or(8);
            let a_max: usize = args.get(4).and_then(|s| s.parse().ok()).unwrap_or(16);

            println!("{:>12} {:>3} {:>3} {:>3} {:>10} {:>6} {:>4} {:>3} {:>10} {:>10}",
                     "Nucleus","Z","N","A","Raw","After","Tgt","Pal","Status","Time");
            println!("{}", "-".repeat(75));

            let t = Instant::now();
            let mut all_opt = true;
            for z in z_min..=z_max {
                let n_min = if z<=1 {1} else {z.saturating_sub(1)};
                for n in n_min..=(z+2) {
                    let a = z+n;
                    if a < 2 || a > a_max { continue; }
                    let r = compute(&engine, z, n);
                    if !r.is_optimal { all_opt = false; }
                    println!("{:>12} {:>3} {:>3} {:>3} {:>10} {:>6} {:>4} {:>3} {:>10} {:>8}ms",
                        r.name, z, n, a, r.raw_terms, r.optimal_terms, r.target,
                        if r.is_palindromic {"Y"} else {" "},
                        if r.is_optimal {"OPTIMAL"} else {"over"}, r.elapsed_ms);
                }
            }
            println!("\nAll optimal: {}  Total: {}ms", if all_opt {"YES"} else {"NO"}, t.elapsed().as_millis());
        }

        "qvalues" => {
            // Beta decay Q-values via transfer matrix (O(A²), no Gröbner expansion)
            let kappa = 0.510999 / 3.0; // m_e / 3 in MeV

            // Shell correction factors (from H₃(q) Markov traces)
            let f_deg2 = 0.5949_f64;
            let f_pauli = 0.6382_f64;
            let magic = [2, 8, 20, 28, 50, 82, 126];

            let shell_degree = |n: usize| -> usize {
                let mut prev = 0;
                for (i, &m) in magic.iter().enumerate() {
                    if n <= m { return if i + 1 >= 5 { 2 } else { 1 }; }
                    prev = m;
                }
                2
            };
            let is_magic = |n: usize| magic.contains(&n);

            struct BenchmarkNucleus { z: usize, n: usize, name: &'static str, q_exp: f64 }
            let benchmarks = [
                BenchmarkNucleus { z: 1, n: 2, name: "³H→³He", q_exp: 0.01861 },
                BenchmarkNucleus { z: 6, n: 8, name: "¹⁴C→¹⁴N", q_exp: 0.15648 },
                BenchmarkNucleus { z: 27, n: 33, name: "⁶⁰Co→⁶⁰Ni", q_exp: 0.31817 },
                BenchmarkNucleus { z: 38, n: 52, name: "⁹⁰Sr→⁹⁰Y", q_exp: 0.54590 },
                BenchmarkNucleus { z: 55, n: 82, name: "¹³⁷Cs→¹³⁷Ba", q_exp: 0.51400 },
                BenchmarkNucleus { z: 83, n: 127, name: "²¹⁰Bi→²¹⁰Po", q_exp: 1.16270 },
            ];

            println!("Q-VALUES FROM OPTIMAL NF (transfer matrix, O(A²))");
            println!("  Proved: NF coeff σ_i = V̂_i (TMCorrespondence)");
            println!("  κ = m_e/3 = {:.6} MeV, q₀ = {:.5}", kappa, engine.q);
            println!();
            println!("{:>16} {:>3} {:>3} {:>8} {:>8} {:>6} {:>8} {:>8} {:>7}",
                "Decay","Z","N","Q_bare","Q_qwt","F_sh","Q_full","Q_exp","Error");
            println!("{}", "-".repeat(78));

            let mut errs = Vec::new();
            for b in &benchmarks {
                // Per-generator volumes for parent and daughter
                let vols_par = engine.generator_volumes(b.z, b.n);
                let vols_dau = engine.generator_volumes(b.z + 1, b.n - 1);

                // Decompose into unbind/rebind
                let a = b.z + b.n;
                let types_par: Vec<u8> = vec![b'p'; b.z].into_iter().chain(vec![b'n'; b.n]).collect();
                let types_dau: Vec<u8> = vec![b'p'; b.z+1].into_iter().chain(vec![b'n'; b.n-1]).collect();

                let mut ln_u = 0.0_f64;
                let mut ln_r = 0.0_f64;
                let mut ln_unc = 0.0_f64;

                for i in 0..a-1 {
                    let vp = vols_par[i];
                    let vd = vols_dau[i];
                    if vp.abs() < 1e-30 || vd.abs() < 1e-30 { continue; }
                    let lr = vd.abs().ln() - vp.abs().ln();

                    let mut changed = Vec::new();
                    for j in i+1..a {
                        let pp = format!("{}{}", types_par[i] as char, types_par[j] as char);
                        let dp = format!("{}{}", types_dau[i] as char, types_dau[j] as char);
                        if pp != dp { changed.push((pp, dp)); }
                    }

                    if changed.is_empty() {
                        ln_unc += lr;
                    } else {
                        let nu: usize = changed.iter().filter(|(p,_)| p == "nn").count();
                        let nr: usize = changed.iter().filter(|(_,d)| d == "pp").count();
                        let t = nu + nr;
                        if nr == 0 { ln_u += lr; }
                        else if nu == 0 { ln_r += lr; }
                        else {
                            ln_u += lr * nu as f64 / t as f64;
                            ln_r += lr * nr as f64 / t as f64;
                        }
                    }
                }

                let lt = ln_u + ln_r + ln_unc;
                let ln_qwt = engine.q * ln_u + (1.0/engine.q) * ln_r + ln_unc;

                let deg = shell_degree(b.n);
                let f_d = if deg >= 2 { f_deg2 } else { 1.0 };
                let f_p = if is_magic(b.n) && deg >= 2 { f_pauli } else { 1.0 };
                let f_sh = f_d * f_p;

                let q_bare = lt.abs() * kappa;
                let q_qwt = ln_qwt.abs() * kappa;
                let q_full = q_qwt * f_sh;
                let err = (q_full - b.q_exp) / b.q_exp * 100.0;
                errs.push(err.abs());

                let mark = if err.abs() < 5.0 { "◀" } else { " " };
                println!("{:>16} {:>3} {:>3} {:>8.5} {:>8.5} {:>6.4} {:>8.5} {:>8.5} {:>+6.1}%{}",
                    b.name, b.z, b.n, q_bare, q_qwt, f_sh, q_full, b.q_exp, err, mark);
            }

            let mae: f64 = errs.iter().sum::<f64>() / errs.len() as f64;
            let rms: f64 = (errs.iter().map(|e| e*e).sum::<f64>() / errs.len() as f64).sqrt();
            println!();
            println!("  MAE = {:.1}%, RMS = {:.1}%", mae, rms);
        }

        _ => { eprintln!("Unknown: {}", args[1]); std::process::exit(1); }
    }
}
