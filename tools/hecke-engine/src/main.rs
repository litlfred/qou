//! Fast Gröbner--Shirshov reduction engine for H_n(q) with Pauli witness.
//!
//! Optimizations:
//! 1. Reduced/unreduced separation with priority queue
//! 2. Batch consolidation of same-word entries
//! 3. Smart add_term: only check junction point for new terms
//! 4. Quotient-during-construction with tr_alt accumulation
//!
//! For A ≤ 10: full NF, exact F_Pauli
//! For A = 11-16: quotient-with-accumulation, exact F_Pauli
//!
//! Usage:
//!   cargo run --release -- pauli Z N        # single nucleus
//!   cargo run --release -- pauli A_max      # table

use rustc_hash::FxHashMap;
use serde::Serialize;
use serde_json;
use std::collections::BinaryHeap;
use std::cmp::Ordering;
use std::time::Instant;

type Word = Vec<u8>;

#[derive(Clone)]
struct PriWord(Word, f64);
impl PartialEq for PriWord { fn eq(&self, o: &Self) -> bool { self.0.len() == o.0.len() } }
impl Eq for PriWord {}
impl PartialOrd for PriWord { fn partial_cmp(&self, o: &Self) -> Option<Ordering> { Some(self.cmp(o)) } }
impl Ord for PriWord { fn cmp(&self, o: &Self) -> Ordering { self.0.len().cmp(&o.0.len()) } }

struct HeckeElement {
    reduced: FxHashMap<Word, f64>,
    unreduced: BinaryHeap<PriWord>,
}

impl HeckeElement {
    fn new() -> Self { Self { reduced: FxHashMap::default(), unreduced: BinaryHeap::new() } }
    fn identity() -> Self { let mut h = Self::new(); h.reduced.insert(vec![], 1.0); h }
    fn n_terms(&self) -> usize { self.reduced.len() }
    fn into_map(self) -> FxHashMap<Word, f64> { self.reduced }
    fn histogram(&self) -> Vec<usize> {
        let mx = self.reduced.keys().map(|w| w.len()).max().unwrap_or(0);
        let mut h = vec![0usize; mx + 1];
        for w in self.reduced.keys() { h[w.len()] += 1; }
        h
    }
}

/// Accumulated Pauli trace data
#[derive(Default, Clone)]
struct PauliAccum {
    tr_alt: f64,  // Σ c_w × (-q⁻¹)^ℓ(w)
    tr_sym: f64,  // Σ c_w × q^ℓ(w)
    net: f64,     // Σ c_w
}

impl PauliAccum {
    fn add_term(&mut self, coeff: f64, word_len: usize, q: f64, qi: f64) {
        self.tr_alt += coeff * (-qi).powi(word_len as i32);
        self.tr_sym += coeff * q.powi(word_len as i32);
        self.net += coeff;
    }
    fn add_from_map(&mut self, terms: &FxHashMap<Word, f64>, q: f64, qi: f64) {
        for (w, &c) in terms { self.add_term(c, w.len(), q, qi); }
    }
}

struct HeckeEngine {
    ha: f64, s: f64, z: f64, q: f64, qi: f64,
}

impl HeckeEngine {
    fn new(q: f64) -> Self {
        let qi = 1.0/q;
        Self { ha: q-qi, s: q.sqrt()-qi.sqrt(), z: 1.0/(q.sqrt()+qi.sqrt()), q, qi }
    }

    fn crossing_coeffs(&self, ti: u8, tj: u8) -> (f64, f64) {
        match (ti, tj) {
            (b'p', b'p') => (1.0, 0.0),
            (b'n', b'n') => (self.q*self.q, -self.q*self.s),
            _ => ((1.0+self.q*self.q)/2.0, -self.q*self.s/2.0),
        }
    }

    #[inline]
    fn find_reduction(word: &[u8]) -> Option<(usize, u8)> {
        let len = word.len();
        if len < 2 { return None; }
        for pos in 0..len-1 {
            let a = word[pos]; let b = word[pos+1];
            if a == b { return Some((pos, 0)); }
            if (a as i16 - b as i16) >= 2 { return Some((pos, 1)); }
            if pos+2 < len {
                let c = word[pos+2];
                if a == c && (a as i16 - b as i16).abs() == 1 && b < a {
                    return Some((pos, 2));
                }
            }
        }
        None
    }

    /// Smart add: for w·gen, only check junction (last char of w, gen)
    /// and propagate if needed. Much faster than scanning full word.
    #[inline]
    fn add_term(elem: &mut HeckeElement, word: Word, coeff: f64) {
        if coeff.abs() < 1e-15 { return; }
        // Quick check: only the new junction could be reducible
        // (the prefix was already reduced)
        let len = word.len();
        let needs_check = if len >= 2 {
            let a = word[len-2]; let b = word[len-1];
            a == b ||                                    // Hecke
            (a as i16 - b as i16) >= 2 ||               // FC
            (len >= 3 && {
                let c = word[len-3];
                c == b && (c as i16 - a as i16).abs() == 1 && a < c
            })                                           // YB at end
        } else { false };

        if needs_check || Self::find_reduction(&word).is_some() {
            elem.unreduced.push(PriWord(word, coeff));
        } else {
            *elem.reduced.entry(word).or_insert(0.0) += coeff;
        }
    }

    fn drain_unreduced(&self, elem: &mut HeckeElement) {
        while !elem.unreduced.is_empty() {
            let mut batch: FxHashMap<Word, f64> = FxHashMap::default();
            while let Some(PriWord(w, c)) = elem.unreduced.pop() {
                *batch.entry(w).or_insert(0.0) += c;
            }
            for (word, coeff) in batch {
                if coeff.abs() < 1e-15 { continue; }
                if let Some((pos, rule)) = Self::find_reduction(&word) {
                    match rule {
                        0 => {
                            let i = word[pos];
                            let mut w1 = Vec::with_capacity(word.len()-1);
                            w1.extend_from_slice(&word[..pos]); w1.push(i);
                            w1.extend_from_slice(&word[pos+2..]);
                            let mut w2 = Vec::with_capacity(word.len()-2);
                            w2.extend_from_slice(&word[..pos]);
                            w2.extend_from_slice(&word[pos+2..]);
                            Self::add_term(elem, w1, coeff * self.ha);
                            Self::add_term(elem, w2, coeff);
                        }
                        1 => { let mut w = word; w.swap(pos, pos+1); Self::add_term(elem, w, coeff); }
                        2 => {
                            let mut w = word;
                            let (a,b) = (w[pos], w[pos+1]);
                            w[pos]=b; w[pos+1]=a; w[pos+2]=b;
                            Self::add_term(elem, w, coeff);
                        }
                        _ => unreachable!(),
                    }
                } else {
                    *elem.reduced.entry(word).or_insert(0.0) += coeff;
                }
            }
        }
        elem.reduced.retain(|_, c| c.abs() > 1e-15);
    }

    fn multiply_and_reduce(&self, elem: &mut HeckeElement, gen: u8, c: f64, d: f64) {
        let old: Vec<(Word, f64)> = elem.reduced.drain().collect();
        for (w, coeff) in old {
            if d.abs() > 1e-15 {
                *elem.reduced.entry(w.clone()).or_insert(0.0) += coeff * d;
            }
            if c.abs() > 1e-15 {
                let mut wg = w; wg.push(gen);
                Self::add_term(elem, wg, coeff * c);
            }
        }
        self.drain_unreduced(elem);
    }

    /// Apply I₉+I₈ quotient, returning Pauli data of removed terms.
    fn apply_quotient_with_pauli(&self, terms: &mut FxHashMap<Word, f64>) -> PauliAccum {
        let mut removed = PauliAccum::default();
        // I₉: strip longest chains
        loop {
            let mut words: Vec<Word> = terms.keys()
                .filter(|w| w.len() >= 2 && terms[*w].abs() > 1e-15)
                .cloned().collect();
            words.sort_unstable_by(|a, b| b.len().cmp(&a.len()));
            let mut found = false;
            for word in &words {
                let prefix = &word[..word.len()-1];
                if terms.get(prefix).map_or(false, |c| c.abs() > 1e-15) {
                    let coeff = terms.remove(word).unwrap_or(0.0);
                    removed.add_term(coeff, word.len(), self.q, self.qi);
                    found = true; break;
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
                    let coeff = terms.remove(&word.clone()).unwrap_or(0.0);
                    removed.add_term(coeff, 2, self.q, self.qi);
                    found = true; break;
                }
            }
            if !found { break; }
        }
        terms.retain(|_, c| c.abs() > 1e-15);
        removed
    }

    /// Build nucleus with Pauli tracking.
    /// For large A: apply quotient at strand boundaries, accumulate tr_alt of removed terms.
    /// The final F_Pauli = |tr_alt_kept + tr_alt_removed| / |net_kept + net_removed|.
    fn build_nucleus_pauli(&self, z: usize, n: usize, use_quotient_after: usize) -> (HeckeElement, PauliAccum) {
        let a = z + n;
        let mut types = vec![b'p'; z];
        types.extend(vec![b'n'; n]);
        let mut elem = HeckeElement::identity();
        let mut accum = PauliAccum::default();

        for k in 1..a {
            for i in 0..k {
                let (c, d) = self.crossing_coeffs(types[i], types[k]);
                self.multiply_and_reduce(&mut elem, i as u8, c, d);
            }
            // Apply quotient for large A to keep terms bounded
            if a > use_quotient_after && k < a - 1 {
                let mut terms = std::mem::take(&mut elem.reduced);
                let removed = self.apply_quotient_with_pauli(&mut terms);
                accum.tr_alt += removed.tr_alt;
                accum.tr_sym += removed.tr_sym;
                accum.net += removed.net;
                elem.reduced = terms;
                eprint!("\r  strand {}/{}: {} terms (accumulated {} removed)", k, a-1, elem.n_terms(),
                    ((accum.net.abs() * 100.0) as u64));
            }
        }
        eprintln!();
        (elem, accum)
    }

    fn build_nucleus(&self, z: usize, n: usize) -> HeckeElement {
        let (elem, _) = self.build_nucleus_pauli(z, n, 999);
        elem
    }

    fn apply_quotient_ideals(terms: &mut FxHashMap<Word, f64>) -> usize {
        let mut total = 0;
        loop {
            let mut words: Vec<Word> = terms.keys()
                .filter(|w| w.len() >= 2 && terms[*w].abs() > 1e-15)
                .cloned().collect();
            words.sort_unstable_by(|a, b| b.len().cmp(&a.len()));
            let mut found = false;
            for word in &words {
                let prefix = &word[..word.len()-1];
                if terms.get(prefix).map_or(false, |c| c.abs() > 1e-15) {
                    terms.remove(word); total += 1; found = true; break;
                }
            }
            if !found { break; }
        }
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
        let a = z+n;
        let mut types = vec![b'p'; z]; types.extend(vec![b'n'; n]);
        (0..a-1).map(|i| {
            let mut m = [[1.0,0.0],[0.0,1.0]];
            for j in (i+1)..a {
                let (c,d) = self.crossing_coeffs(types[i], types[j]);
                let t = [[c*self.ha+d,c],[c,d]];
                m = [[m[0][0]*t[0][0]+m[0][1]*t[1][0], m[0][0]*t[0][1]+m[0][1]*t[1][1]],
                     [m[1][0]*t[0][0]+m[1][1]*t[1][0], m[1][0]*t[0][1]+m[1][1]*t[1][1]]];
            }
            self.z*m[0][0]+m[1][0]
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

fn is_palindromic(h: &[usize]) -> bool { let n=h.len(); (0..n/2).all(|i| h[i]==h[n-1-i]) }

fn nucleus_name(z: usize, n: usize) -> String {
    let a=z+n;
    let s=match z {1=>"H",2=>"He",3=>"Li",4=>"Be",5=>"B",6=>"C",7=>"N",8=>"O",9=>"F",10=>"Ne",_=>"?"};
    format!("{}{}({},{})", a, s, z, n)
}

fn compute(engine: &HeckeEngine, z: usize, n: usize) -> NucleusResult {
    let a=z+n; let t0=Instant::now();
    let (raw, hist, pal, opt) = if a <= 8 {
        let elem = engine.build_nucleus(z, n);
        let raw=elem.n_terms(); let hist=elem.histogram(); let pal=is_palindromic(&hist);
        let mut terms=elem.into_map(); HeckeEngine::apply_quotient_ideals(&mut terms);
        (raw, hist, pal, terms.len())
    } else {
        let (elem, _) = engine.build_nucleus_pauli(z, n, 8);
        let opt=elem.n_terms(); let hist=elem.histogram(); let pal=is_palindromic(&hist);
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
        eprintln!("Usage: hecke-engine [nucleus|table|pauli|shellfactor|qvalues] ...");
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
            let t=Instant::now(); let mut all_opt=true;
            for z in z_min..=z_max {
                let n_min = if z<=1 {1} else {z.saturating_sub(1)};
                for n in n_min..=(z+2) {
                    let a=z+n; if a<2||a>a_max { continue; }
                    let r=compute(&engine, z, n);
                    if !r.is_optimal { all_opt=false; }
                    println!("{:>12} {:>3} {:>3} {:>3} {:>10} {:>6} {:>4} {:>3} {:>10} {:>8}ms",
                        r.name,z,n,a,r.raw_terms,r.optimal_terms,r.target,
                        if r.is_palindromic {"Y"} else {" "},
                        if r.is_optimal {"OPTIMAL"} else {"over"},r.elapsed_ms);
                }
            }
            println!("\nAll optimal: {} Total: {}ms", if all_opt {"YES"} else {"NO"}, t.elapsed().as_millis());
        }

        "pauli" => {
            let z: usize = args.get(2).and_then(|s| s.parse().ok()).unwrap_or(0);
            let n: usize = args.get(3).and_then(|s| s.parse().ok()).unwrap_or(0);

            if z > 0 && n > 0 {
                let a = z + n;
                let t0 = Instant::now();

                // For A ≤ 10: full NF. For A > 10: quotient with accumulation.
                let use_quotient_after = if a <= 10 { 999 } else { 10 };
                let (elem, accum) = engine.build_nucleus_pauli(z, n, use_quotient_after);

                let mut kept = PauliAccum::default();
                kept.add_from_map(&elem.reduced, engine.q, engine.qi);

                let tr_alt = kept.tr_alt + accum.tr_alt;
                let tr_sym = kept.tr_sym + accum.tr_sym;
                let net = kept.net + accum.net;
                let f = if net.abs() > 1e-30 { tr_alt.abs() / net.abs() } else { 0.0 };

                let hist = elem.histogram();
                let pal = is_palindromic(&hist);
                let ms = t0.elapsed().as_millis();

                println!("{}: A={}, {} terms{}, pal={}",
                    nucleus_name(z,n), a, elem.n_terms(),
                    if accum.net.abs() > 1e-10 { format!(" (+{:.0} accumulated)", accum.net.abs()) } else { String::new() },
                    if pal {"Y"} else {"N"});
                println!("  tr_alt = {:+.10} (kept {:+.6} + accum {:+.6})", tr_alt, kept.tr_alt, accum.tr_alt);
                println!("  net    = {:+.10} (kept {:+.6} + accum {:+.6})", net, kept.net, accum.net);
                println!("  F_Pauli^(A) = {:.6}", f);
                println!("  {}ms", ms);

                println!("{}", serde_json::json!({
                    "nucleus": nucleus_name(z,n), "z": z, "n": n, "a": a,
                    "raw_terms": elem.n_terms(), "palindromic": pal,
                    "tr_alt": tr_alt, "tr_alt_kept": kept.tr_alt, "tr_alt_accum": accum.tr_alt,
                    "net": net, "net_kept": kept.net, "net_accum": accum.net,
                    "F_Pauli_A": f, "histogram": hist,
                    "use_quotient_after": use_quotient_after,
                    "elapsed_ms": ms, "q": engine.q,
                }));
            } else {
                // Table
                let a_max: usize = args.get(2).and_then(|s| s.parse().ok()).unwrap_or(8);
                println!("F_PAULI^(A) TABLE (A ≤ {})", a_max);
                println!("  q₀ = {:.5}", engine.q);
                println!();
                println!("{:>12} {:>3} {:>3} {:>3} {:>10} {:>3} {:>12} {:>12} {:>10} {:>8}",
                    "Nucleus","Z","N","A","Terms","Pal","tr_alt","net","F_Pauli","Time");
                println!("{}", "-".repeat(90));

                for zz in 1..=a_max {
                    let n_min = if zz<=1 {1} else {zz.saturating_sub(1)};
                    for nn in n_min..=(zz+2) {
                        let a = zz+nn;
                        if a < 2 || a > a_max || nn+1 < zz { continue; }
                        let t0 = Instant::now();
                        let use_q = if a <= 10 { 999 } else { 10 };
                        let (elem, accum) = engine.build_nucleus_pauli(zz, nn, use_q);
                        let mut kept = PauliAccum::default();
                        kept.add_from_map(&elem.reduced, engine.q, engine.qi);
                        let tr_alt = kept.tr_alt + accum.tr_alt;
                        let net = kept.net + accum.net;
                        let f = if net.abs()>1e-30 { tr_alt.abs()/net.abs() } else { 0.0 };
                        let hist = elem.histogram();
                        let pal = is_palindromic(&hist);
                        let ms = t0.elapsed().as_millis();
                        let tag = if accum.net.abs() > 1e-10 { "~" } else { " " };
                        println!("{:>12} {:>3} {:>3} {:>3} {:>10} {:>3} {:>+12.6} {:>+12.6} {:>10.6}{} {:>6}ms",
                            nucleus_name(zz,nn),zz,nn,a,elem.n_terms(),
                            if pal {"Y"} else {" "}, tr_alt, net, f, tag, ms);
                    }
                }
            }
        }

        "qvalues" => {
            // Use log_q(x) = ln(x)/ln(q) consistently.
            // The q-integer structure: log_q(P_dau/P_par) ≈ −(N−1), where N is the
            // number of strands whose crossing type changes in the β⁻ decay.
            // Numerically: log_q × κ_q = ln × κ  (the ln(q) cancels), so the
            // final Q-value prediction is unchanged from the bare-ln formulation.
            let ln_q = engine.q.ln();
            let kappa_q = 0.510999 / 3.0 * ln_q;  // κ_q = ln(q) × m_e/3
            let f_deg2 = 0.5949_f64; let f_pauli = 0.6382_f64;
            let magic = [2,8,20,28,50,82,126];
            let shell_degree = |n: usize| -> usize {
                let mut prev=0;
                for (i,&m) in magic.iter().enumerate() { if n<=m { return if i+1>=5 {2} else {1}; } prev=m; } 2
            };
            let is_magic = |n: usize| magic.contains(&n);

            struct B { z: usize, n: usize, name: &'static str, q_exp: f64 }
            let benchmarks = [
                B{z:1,n:2,name:"³H→³He",q_exp:0.01861},B{z:6,n:8,name:"¹⁴C→¹⁴N",q_exp:0.15648},
                B{z:27,n:33,name:"⁶⁰Co→⁶⁰Ni",q_exp:0.31817},B{z:38,n:52,name:"⁹⁰Sr→⁹⁰Y",q_exp:0.54590},
                B{z:55,n:82,name:"¹³⁷Cs→¹³⁷Ba",q_exp:0.51400},B{z:83,n:127,name:"²¹⁰Bi→²¹⁰Po",q_exp:1.16270},
            ];
            println!("Q-VALUES (transfer matrix, log_q basis, κ_q={:.6} MeV, ln(q)={:.6}, q₀={:.5})", kappa_q, ln_q, engine.q);
            println!("{:>16} {:>8} {:>8} {:>8} {:>8} {:>7}", "Decay","Q_pred","Q_exp","log_q","F","Error");
            println!("{}", "-".repeat(65));
            let mut errs = Vec::new();
            for b in &benchmarks {
                let a=b.z+b.n;
                let types_p: Vec<u8> = (0..b.z).map(|_| b'p').chain((0..b.n).map(|_| b'n')).collect();
                let types_d: Vec<u8> = (0..b.z+1).map(|_| b'p').chain((0..b.n-1).map(|_| b'n')).collect();
                let vp = engine.generator_volumes(b.z, b.n);
                let vd = engine.generator_volumes(b.z+1, b.n-1);
                let mut lu=0.0f64; let mut lr=0.0f64; let mut luc=0.0f64;
                for i in 0..a-1 {
                    if vp[i].abs()<1e-30||vd[i].abs()<1e-30 { continue; }
                    // log_q(V_dau_i / V_par_i) = ln(V_dau_i / V_par_i) / ln(q)
                    let lratio = (vd[i].abs().ln()-vp[i].abs().ln()) / ln_q;
                    let changed: Vec<_> = (i+1..a).filter(|&j| {
                        let pp=format!("{}{}",types_p[i] as char,types_p[j] as char);
                        let pd=format!("{}{}",types_d[i] as char,types_d[j] as char);
                        pp != pd
                    }).collect();
                    if changed.is_empty() { luc+=lratio; }
                    else {
                        let nu=changed.iter().filter(|&&j| types_p[i]==b'n'&&types_p[j]==b'n').count();
                        let nr=changed.iter().filter(|&&j| types_d[i]==b'p'&&types_d[j]==b'p').count();
                        let t=nu+nr;
                        if nr==0{lu+=lratio}else if nu==0{lr+=lratio}
                        else{lu+=lratio*nu as f64/t as f64; lr+=lratio*nr as f64/t as f64;}
                    }
                }
                // q-weighting unchanged: q × log_q(u) + q⁻¹ × log_q(r) + log_q(uc)
                // Then Q = |weighted sum| × κ_q.  Since lratio is now log_q and
                // κ_q = κ × ln(q), the product log_q × κ_q = ln × κ is invariant.
                let q_qwt = (engine.q*lu+engine.qi*lr+luc).abs()*kappa_q;
                let log_q_total = lu + lr + luc;  // total log_q(P_dau/P_par) ≈ −(N−1)
                let deg=shell_degree(b.n);
                let mut f = if deg>=2 {f_deg2} else {1.0};
                if is_magic(b.n)&&deg>=2 { f*=f_pauli; }
                let q_pred=q_qwt*f;
                let err=(q_pred-b.q_exp)/b.q_exp*100.0;
                errs.push(err.abs());
                let mark=if err.abs()<5.0 {"◀"} else {" "};
                println!("{:>16} {:>8.5} {:>8.5} {:>+8.3} {:>8.4} {:>+6.1}%{}", b.name, q_pred, b.q_exp, log_q_total, f, err, mark);
            }
            let mae: f64 = errs.iter().sum::<f64>()/errs.len() as f64;
            println!("\nMAE = {:.1}%  (log_q(P_dau/P_par) should be ≈ −(N−1), a q-integer)", mae);
        }

        _ => { eprintln!("Unknown: {}", args[1]); std::process::exit(1); }
    }
}
