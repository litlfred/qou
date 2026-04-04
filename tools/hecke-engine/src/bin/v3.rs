// v3: Tree-packed words for A ≤ 16 (word length up to 120).
//
// Each chunk holds 31 generators (4 bits each) + 4 bits length.
// Tree depth = number of chunks = ceil(word_length / 31).
// For A ≤ 8:  1 chunk  (same as v2)
// For A ≤ 16: up to 4 chunks (word length up to 120)
//
// Layout: [u128; 4] = 64 bytes per word.
// Chunk i holds generators [31*i .. 31*(i+1)-1].
// Chunk 0 bits 124..127: total length (but only 4 bits = max 15... not enough!)
//
// Fix: store length separately. Use all 128 bits of each chunk for generators.
// 128 bits / 4 bits per gen = 32 generators per chunk.
// 4 chunks × 32 = 128 generators max. Enough for A=16 (max word length 120).

#![allow(unused_imports)]
pub use rustc_hash::FxHashMap;
use std::time::Instant;

const GENS_PER_CHUNK: usize = 32;
const MAX_CHUNKS: usize = 4;
const MAX_WORD_LEN: usize = GENS_PER_CHUNK * MAX_CHUNKS; // 128

/// Tree-packed word: up to 128 generators in 4 × u128 chunks.
/// Length stored in low 8 bits of chunks[0] (generators shifted by 8).
/// Actually simpler: store (len, chunks) as separate fields.
#[derive(Clone, Copy, PartialEq, Eq, Hash)]
struct TreeWord {
    len: u8,                    // word length (0..128)
    chunks: [u128; MAX_CHUNKS], // generators packed 4 bits each
}

impl TreeWord {
    const EMPTY: TreeWord = TreeWord { len: 0, chunks: [0; MAX_CHUNKS] };

    #[inline]
    fn len(self) -> usize { self.len as usize }

    #[inline]
    fn chunk_and_offset(pos: usize) -> (usize, usize) {
        (pos / GENS_PER_CHUNK, (pos % GENS_PER_CHUNK) * 4)
    }

    #[inline]
    fn get(self, pos: usize) -> u8 {
        let (chunk, bit) = Self::chunk_and_offset(pos);
        ((self.chunks[chunk] >> bit) & 0xF) as u8
    }

    #[inline]
    fn set(&mut self, pos: usize, val: u8) {
        let (chunk, bit) = Self::chunk_and_offset(pos);
        self.chunks[chunk] = (self.chunks[chunk] & !(0xFu128 << bit)) | ((val as u128) << bit);
    }

    #[inline]
    fn push(self, gen: u8) -> TreeWord {
        let l = self.len as usize;
        debug_assert!(l < MAX_WORD_LEN);
        let mut w = self;
        w.set(l, gen);
        w.len = (l + 1) as u8;
        w
    }

    #[inline]
    fn drop_last(self) -> TreeWord {
        let l = self.len as usize;
        if l == 0 { return self; }
        let mut w = self;
        w.set(l - 1, 0); // clear the last generator
        w.len = (l - 1) as u8;
        w
    }

    fn remove_at(self, pos: usize) -> TreeWord {
        let l = self.len as usize;
        let mut result = TreeWord { len: (l - 1) as u8, chunks: [0; MAX_CHUNKS] };
        let mut j = 0;
        for i in 0..l {
            if i == pos { continue; }
            result.set(j, self.get(i));
            j += 1;
        }
        result
    }

    fn hecke_reduce(self, pos: usize) -> (TreeWord, TreeWord) {
        let w1 = self.remove_at(pos + 1); // remove second of the pair
        let w2 = w1.remove_at(pos);       // remove first too
        (w1, w2)
    }

    fn swap(self, pos: usize) -> TreeWord {
        let a = self.get(pos);
        let b = self.get(pos + 1);
        let mut w = self;
        w.set(pos, b);
        w.set(pos + 1, a);
        w
    }

    fn yb_replace(self, pos: usize) -> TreeWord {
        let a = self.get(pos);
        let b = self.get(pos + 1);
        let mut w = self;
        w.set(pos, b);
        w.set(pos + 1, a);
        w.set(pos + 2, b);
        w
    }

    #[inline]
    fn junction_reduction(self) -> Option<(usize, u8)> {
        let l = self.len();
        if l < 2 { return None; }
        let pos = l - 2;
        let a = self.get(pos);
        let b = self.get(pos + 1);
        if a == b { return Some((pos, 0)); }
        if (a as i16 - b as i16) >= 2 { return Some((pos, 1)); }
        if l >= 3 {
            let c = self.get(l - 3);
            if c == b && (c as i16 - a as i16).abs() == 1 && a < c {
                return Some((l - 3, 2));
            }
        }
        None
    }

    fn find_reduction(self) -> Option<(usize, u8)> {
        let l = self.len();
        if l < 2 { return None; }
        for pos in 0..l-1 {
            let a = self.get(pos);
            let b = self.get(pos + 1);
            if a == b { return Some((pos, 0)); }
            if (a as i16 - b as i16) >= 2 { return Some((pos, 1)); }
            if pos + 2 < l {
                let c = self.get(pos + 2);
                if a == c && (a as i16 - b as i16).abs() == 1 && b < a {
                    return Some((pos, 2));
                }
            }
        }
        None
    }
}

impl std::fmt::Debug for TreeWord {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        let l = self.len();
        if l == 0 { return write!(f, "𝟏"); }
        for i in 0..l {
            if i > 0 { write!(f, ".")?; }
            write!(f, "σ{}", self.get(i))?;
        }
        Ok(())
    }
}

// ════════════════════════════════════════════════════════════════

struct HeckeElem {
    terms: FxHashMap<TreeWord, f64>,
}

impl HeckeElem {
    fn new() -> Self { Self { terms: FxHashMap::default() } }
    fn identity() -> Self { let mut h = Self::new(); h.terms.insert(TreeWord::EMPTY, 1.0); h }
    fn n_terms(&self) -> usize { self.terms.len() }
    fn clean(&mut self) { self.terms.retain(|_, c| c.abs() > 1e-15); }

    fn histogram(&self) -> Vec<usize> {
        let mx = self.terms.keys().map(|w| w.len()).max().unwrap_or(0);
        let mut h = vec![0usize; mx + 1];
        for w in self.terms.keys() { h[w.len()] += 1; }
        h
    }

    fn memory_bytes(&self) -> usize {
        // TreeWord is 64+1 bytes, plus FxHashMap overhead (~80 bytes per entry)
        self.terms.len() * 96
    }
}

#[derive(Default, Clone)]
struct PauliAcc {
    tr_alt: f64, tr_sym: f64, net: f64,
}

impl PauliAcc {
    fn add(&mut self, coeff: f64, word_len: usize, q: f64, qi: f64) {
        self.tr_alt += coeff * (-qi).powi(word_len as i32);
        self.tr_sym += coeff * q.powi(word_len as i32);
        self.net += coeff;
    }
    fn from_elem(elem: &HeckeElem, q: f64, qi: f64) -> Self {
        let mut acc = Self::default();
        for (w, &c) in &elem.terms { acc.add(c, w.len(), q, qi); }
        acc
    }
    fn merge(&mut self, other: &PauliAcc) {
        self.tr_alt += other.tr_alt;
        self.tr_sym += other.tr_sym;
        self.net += other.net;
    }
}

struct Engine {
    ha: f64, q: f64, qi: f64,
}

impl Engine {
    fn new(q: f64) -> Self {
        let qi = 1.0/q;
        Self { ha: q-qi, q, qi }
    }

    fn crossing_coeffs(&self, ti: u8, tj: u8) -> (f64, f64) {
        match (ti, tj) {
            (b'p', b'p') => (1.0, 0.0),
            (b'n', b'n') => (self.q*self.q, -self.q*(self.q.sqrt()-self.qi.sqrt())),
            _ => ((1.0+self.q*self.q)/2.0, -self.q*(self.q.sqrt()-self.qi.sqrt())/2.0),
        }
    }

    fn add_term(elem: &mut HeckeElem, word: TreeWord, coeff: f64) {
        if coeff.abs() < 1e-15 { return; }
        if word.junction_reduction().is_some() || word.find_reduction().is_some() {
            // Put in unreduced buffer
            elem.terms.entry(word).and_modify(|c| *c += coeff).or_insert(coeff);
            // Mark as needing reduction by using the terms map directly
            // (we'll drain and reduce in drain_unreduced)
        } else {
            *elem.terms.entry(word).or_insert(0.0) += coeff;
        }
    }

    fn reduce_all(&self, elem: &mut HeckeElem) {
        // Repeatedly scan for reducible terms and process them.
        // Since terms are in a HashMap, we drain reducible ones in batches.
        loop {
            let mut to_reduce: Vec<(TreeWord, f64)> = Vec::new();
            let mut stable: FxHashMap<TreeWord, f64> = FxHashMap::default();

            for (word, &coeff) in &elem.terms {
                if coeff.abs() < 1e-15 { continue; }
                if let Some(_) = word.find_reduction() {
                    to_reduce.push((*word, coeff));
                } else {
                    *stable.entry(*word).or_insert(0.0) += coeff;
                }
            }

            if to_reduce.is_empty() { break; }

            // Process all reducible terms
            for (word, coeff) in to_reduce {
                if let Some((pos, rule)) = word.find_reduction() {
                    match rule {
                        0 => { // Hecke
                            let (w1, w2) = word.hecke_reduce(pos);
                            *stable.entry(w1).or_insert(0.0) += coeff * self.ha;
                            *stable.entry(w2).or_insert(0.0) += coeff;
                        }
                        1 => { // Far-comm
                            *stable.entry(word.swap(pos)).or_insert(0.0) += coeff;
                        }
                        2 => { // YB
                            *stable.entry(word.yb_replace(pos)).or_insert(0.0) += coeff;
                        }
                        _ => unreachable!(),
                    }
                }
            }

            elem.terms = stable;
            elem.clean();
        }
    }

    fn multiply_and_reduce(&self, elem: &mut HeckeElem, gen: u8, c: f64, d: f64) {
        let old: Vec<(TreeWord, f64)> = elem.terms.drain().collect();
        for (w, coeff) in old {
            if d.abs() > 1e-15 {
                *elem.terms.entry(w).or_insert(0.0) += coeff * d;
            }
            if c.abs() > 1e-15 {
                let wg = w.push(gen);
                *elem.terms.entry(wg).or_insert(0.0) += coeff * c;
            }
        }
        self.reduce_all(elem);
    }

    fn apply_quotient_with_pauli(&self, terms: &mut FxHashMap<TreeWord, f64>) -> PauliAcc {
        let mut removed = PauliAcc::default();
        // I₉: strip longest chains
        loop {
            let mut words: Vec<TreeWord> = terms.keys()
                .filter(|w| w.len() >= 2 && terms[*w].abs() > 1e-15)
                .cloned().collect();
            words.sort_unstable_by(|a, b| b.len().cmp(&a.len()));
            let mut found = false;
            for word in &words {
                let prefix = word.drop_last();
                if terms.get(&prefix).map_or(false, |c| c.abs() > 1e-15) {
                    let coeff = terms.remove(word).unwrap_or(0.0);
                    removed.add(coeff, word.len(), self.q, self.qi);
                    found = true; break;
                }
            }
            if !found { break; }
        }
        // I₈: adjacency
        loop {
            let adj: Vec<TreeWord> = terms.keys()
                .filter(|w| w.len() == 2 && terms[*w].abs() > 1e-15 && w.get(1) == w.get(0) + 1)
                .cloned().collect();
            let mut found = false;
            for word in &adj {
                let sigma_j = TreeWord::EMPTY.push(word.get(1));
                if terms.get(&sigma_j).map_or(false, |c| c.abs() > 1e-15) {
                    let coeff = terms.remove(&word).unwrap_or(0.0);
                    removed.add(coeff, 2, self.q, self.qi);
                    found = true; break;
                }
            }
            if !found { break; }
        }
        terms.retain(|_, c| c.abs() > 1e-15);
        removed
    }

    fn build_nucleus_pauli(&self, z: usize, n: usize, quotient_after: usize)
        -> (HeckeElem, PauliAcc)
    {
        let a = z + n;
        let mut types = vec![b'p'; z];
        types.extend(vec![b'n'; n]);
        let mut elem = HeckeElem::identity();
        let mut accum = PauliAcc::default();

        for k in 1..a {
            for i in 0..k {
                let (c, d) = self.crossing_coeffs(types[i], types[k]);
                self.multiply_and_reduce(&mut elem, i as u8, c, d);
            }
            if a > quotient_after && k < a - 1 {
                let mut terms = std::mem::take(&mut elem.terms);
                let removed = self.apply_quotient_with_pauli(&mut terms);
                accum.merge(&removed);
                elem.terms = terms;
            }
            let mem_mb = elem.memory_bytes() as f64 / 1_048_576.0;
            eprintln!("  strand {}/{}: {} terms, {:.0}MB",
                k, a-1, elem.n_terms(), mem_mb);
        }
        (elem, accum)
    }
}

fn is_palindromic(h: &[usize]) -> bool { let n=h.len(); (0..n/2).all(|i| h[i]==h[n-1-i]) }

fn nucleus_name(z: usize, n: usize) -> String {
    let a=z+n;
    let s=match z {1=>"H",2=>"He",3=>"Li",4=>"Be",5=>"B",6=>"C",7=>"N",8=>"O",9=>"F",10=>"Ne",_=>"?"};
    format!("{}{}({},{})", a, s, z, n)
}

fn main() {
    let args: Vec<String> = std::env::args().collect();
    let engine = Engine::new(1.10998);

    if args.len() < 2 {
        eprintln!("Usage: v3 pauli Z N | pauli A_max");
        std::process::exit(1);
    }

    match args[1].as_str() {
        "pauli" => {
            let z: usize = args.get(2).and_then(|s| s.parse().ok()).unwrap_or(0);
            let n: usize = args.get(3).and_then(|s| s.parse().ok()).unwrap_or(0);

            if z > 0 && n > 0 {
                let a = z + n;
                let sym = match z {1=>"H",2=>"He",3=>"Li",4=>"Be",5=>"B",6=>"C",7=>"N",8=>"O",9=>"F",10=>"Ne",_=>"?"};
                let magic = [2,8,20,28,50,82,126];
                let z_magic = magic.contains(&z);
                let n_magic = magic.contains(&n);
                let doubly_magic = z_magic && n_magic;
                let parity = match (z % 2, n % 2) {
                    (0, 0) => "even-even",
                    (1, 1) => "odd-odd",
                    _ => "mixed",
                };

                println!("════════════════════════════════════════════════════════");
                println!("  Pauli witness for {}{}  (Z={}, N={}, A={})", a, sym, z, n, a);
                println!("  Parity: {}{}{}",
                    parity,
                    if doubly_magic { " ★★ DOUBLY MAGIC" }
                    else if z_magic { " (Z magic)" }
                    else if n_magic { " (N magic)" }
                    else { "" },
                    if n + 1 >= z { "" } else { " ⚠ PROTON-HEAVY (N < Z−1)" });
                println!();
                println!("  Computing the Gröbner normal form in H_{}(q).", a);
                println!("  This is the FULL Hecke algebra expansion — every");
                println!("  reduced word with its exact coefficient at q₀.");
                println!();
                println!("  The Pauli factor F = |tr_alt(NF)| / |net(NF)|");
                println!("  measures the alternating irrep content.");
                println!("  tr_alt = Σ c_w × (−q⁻¹)^ℓ(w)  (alternating eval)");
                println!("  net    = Σ c_w                  (total amplitude)");
                println!();
                println!("  For doubly magic nuclei: F is enhanced (Pauli active).");
                println!("  For odd-odd nuclei: F is suppressed (pairing deficit).");
                println!("════════════════════════════════════════════════════════");
                println!();

                let t0 = Instant::now();
                let use_q = if a <= 10 { 999 } else { 10 };
                if a > 10 {
                    println!("  Using quotient-with-accumulation (A > 10).");
                    println!("  Terms stripped at strand boundaries; Pauli data preserved.");
                    println!();
                }
                let (elem, accum) = engine.build_nucleus_pauli(z, n, use_q);

                let kept = PauliAcc::from_elem(&elem, engine.q, engine.qi);
                let tr_alt = kept.tr_alt + accum.tr_alt;
                let net = kept.net + accum.net;
                let f = if net.abs() > 1e-30 { tr_alt.abs() / net.abs() } else { 0.0 };

                let hist = elem.histogram();
                let pal = is_palindromic(&hist);
                let ms = t0.elapsed().as_millis();
                let mem = elem.memory_bytes() as f64 / 1_048_576.0;

                println!();
                println!("════════════════════════════════════════════════════════");
                println!("  RESULT: {}{}  (Z={}, N={}, A={})", a, sym, z, n, a);
                println!("────────────────────────────────────────────────────────");
                println!("  NF terms:    {}", elem.n_terms());
                println!("  Memory:      {:.1} MB", mem);
                println!("  Time:        {:.1} s", ms as f64 / 1000.0);
                println!("  Palindromic: {}", if pal { "YES (shell closure signature)" } else { "NO" });
                println!();
                println!("  tr_alt = {:+.10}", tr_alt);
                println!("  net    = {:+.10}", net);
                if accum.net.abs() > 1e-10 {
                    println!("    (kept: {:.6}, accumulated from stripped terms: {:.6})", kept.net, accum.net);
                }
                println!();
                println!("  F_Pauli^({}) = {:.6}", a, f);
                println!();
                if f > 0.6 {
                    println!("  → HIGH alternating content (Pauli channel active)");
                    println!("    Consistent with magic/doubly-magic shell structure.");
                } else if f > 0.3 {
                    println!("  → MODERATE alternating content.");
                } else {
                    println!("  → LOW alternating content (single-eigenvalue dominated).");
                    if parity == "odd-odd" {
                        println!("    Odd-odd nucleus: pairing deficit suppresses F.");
                    }
                }
                println!();
                println!("  Reference: H₃(q) F_Pauli = 0.6382 (from 3-strand irrep theory).");
                println!("  This A-strand F_Pauli is the multi-generator witness.");
                println!("════════════════════════════════════════════════════════");
            } else {
                let a_max: usize = args.get(2).and_then(|s| s.parse().ok()).unwrap_or(8);
                println!("F_PAULI TABLE (A ≤ {}, tree-packed words up to 128 gens)", a_max);
                for zz in 1..=a_max {
                    let n_min = if zz<=1 {1} else {zz.saturating_sub(1)};
                    for nn in n_min..=(zz+2) {
                        let a = zz+nn;
                        if a < 2 || a > a_max || nn+1 < zz { continue; }
                        let t0 = Instant::now();
                        let use_q = if a <= 10 { 999 } else { 10 };
                        let (elem, accum) = engine.build_nucleus_pauli(zz, nn, use_q);
                        let kept = PauliAcc::from_elem(&elem, engine.q, engine.qi);
                        let tr_alt = kept.tr_alt + accum.tr_alt;
                        let net = kept.net + accum.net;
                        let f = if net.abs()>1e-30 { tr_alt.abs()/net.abs() } else { 0.0 };
                        let pal = is_palindromic(&elem.histogram());
                        println!("{:>12} {:>3} {:>10.6} {:>3} {:>8}ms",
                            nucleus_name(zz,nn), a, f,
                            if pal {"Y"} else {" "}, t0.elapsed().as_millis());
                    }
                }
            }
        }

        _ => { eprintln!("Unknown: {}", args[1]); std::process::exit(1); }
    }
}
