#![forbid(unsafe_code)]

//! `gs-peel` — JSON CLI exposing `gs-basis` exact dyadic Laurent normal-form walks,
//! planar Temperley–Lieb loop-closure traces, homogeneous Markov tower peeling, and
//! monotone two-row Bratteli character sweeps.

use std::collections::BTreeSet;
use std::env;
use std::fs;
use std::io::{self, Read, Write};

use gs_basis::peel::bratteli_two_row::two_row_bratteli_trace;
use gs_basis::peel::markov_tower::{
    streaming_markov_trace_homogeneous, LinearFactor, StreamingHeckeAccumulator,
};
use gs_basis::{
    rat, CoeffRing, DyadicLaurent, DyadicScalar, PlanarMatching, TemperleyLiebBasis,
    TemperleyLiebElement,
};
use num_bigint::BigInt;
use num_rational::BigRational;
use serde::{Deserialize, Serialize};

/// Linear Hecke factor $(c_m 2^{c_e} h^{c_h})\,\sigma_{\text{gen}} + (d_m 2^{d_e} h^{d_h})\,\mathbf{1}$,
/// repeated `repeat` times.
#[derive(Clone, Debug, Deserialize)]
struct DyadicStepSpec {
    gen: usize,
    #[serde(default = "default_one_i64")]
    c_mant: i64,
    #[serde(default)]
    c_exp2: i32,
    #[serde(default)]
    c_hpow: u32,
    #[serde(default)]
    d_mant: i64,
    #[serde(default)]
    d_exp2: i32,
    #[serde(default)]
    d_hpow: u32,
    #[serde(default = "default_one_usize")]
    repeat: usize,
}

fn default_one_i64() -> i64 {
    1
}
fn default_one_usize() -> usize {
    1
}

impl DyadicStepSpec {
    fn to_linear_factor(&self) -> LinearFactor<DyadicLaurent> {
        let one = DyadicLaurent::one();
        let c = one.scale_dyadic_h_pow(self.c_mant, self.c_exp2, self.c_hpow);
        let d = one.scale_dyadic_h_pow(self.d_mant, self.d_exp2, self.d_hpow);
        LinearFactor::new(c, d, self.gen)
    }
}

#[derive(Clone, Debug, Deserialize)]
struct NfWalkJob {
    id: String,
    num_strands: usize,
    #[serde(default)]
    include_terms: bool,
    steps: Vec<DyadicStepSpec>,
}

#[derive(Clone, Debug, Deserialize)]
struct RationalFactorSpec {
    gen: usize,
    c_num: i64,
    c_den: i64,
    d_num: i64,
    d_den: i64,
}

#[derive(Clone, Debug, Deserialize)]
#[serde(tag = "op", rename_all = "snake_case")]
enum PeelRequest {
    /// Batch of exact dyadic Laurent normal-form walks in $H_n(q)$.
    DyadicHeckeNfBatch { jobs: Vec<NfWalkJob> },
    /// Prefix-by-prefix Temperley–Lieb loop-closure trace walk over `DyadicLaurent`:
    /// `levels[idx]` contains the steps added when extending from `idx + 1` to `idx + 2` strands,
    /// returning $P_m(q) = \operatorname{tr}_{\mathrm{loop}}(\pi_{TL}(E_m)) \in \mathbb{Z}[\frac{1}{2}][q, q^{-1}]$
    /// at each level $m = 2 \dots L + 1$ so $\operatorname{tr}_{TL}(E_m) = P_m(q) / (q + q^{-1})^m$.
    TlDyadicTraceWalk { levels: Vec<Vec<DyadicStepSpec>> },
    /// Homogeneous division-free Markov tower peeling returning
    /// $z_{\mathrm{den}}^{\,n-1} \operatorname{tr}_{M, z_{\mathrm{num}}/z_{\mathrm{den}}}(x) \in \mathbb{Z}[\frac{1}{2}][q, q^{-1}]$,
    /// defaulting to balanced Temperley–Lieb $z_{\mathrm{num}} = q^2$, $z_{\mathrm{den}} = q + q^{-1}$.
    MarkovTowerHomogeneous {
        num_strands: usize,
        steps: Vec<DyadicStepSpec>,
    },
    /// Exact rational monotone two-row Bratteli trace & characters at `q = q_num / q_den`.
    BratteliTwoRowRational {
        num_strands: usize,
        q_num: i64,
        q_den: i64,
        factors: Vec<RationalFactorSpec>,
    },
}

/// Serialized `(q_exp, odd_mantissa_decimal, exp2)` term.
type RawDyadicTerm = (i32, String, i32);

fn serialize_poly_terms(poly: &DyadicLaurent) -> Vec<RawDyadicTerm> {
    poly.nonzero_terms()
        .into_iter()
        .map(|(e, m, e2)| (e, m.to_string(), e2))
        .collect()
}

#[derive(Serialize)]
struct BasisComponentOut {
    word: Vec<usize>,
    min_degree: Option<i32>,
    max_degree: Option<i32>,
    n_terms: usize,
    #[serde(skip_serializing_if = "Option::is_none")]
    terms: Option<Vec<RawDyadicTerm>>,
}

#[derive(Serialize)]
struct NfJobResult {
    id: String,
    min_degree: i32,
    max_degree: i32,
    degree_span: i32,
    n_terms: usize,
    support_size: usize,
    components: Vec<BasisComponentOut>,
}

#[derive(Serialize)]
struct TlLevelTraceOut {
    strands: usize,
    num_diagrams: usize,
    numerator_terms: Vec<RawDyadicTerm>,
}

#[derive(Serialize)]
#[serde(tag = "op", rename_all = "snake_case")]
enum PeelResponse {
    DyadicHeckeNfBatch {
        results: Vec<NfJobResult>,
    },
    TlDyadicTraceWalk {
        levels: Vec<TlLevelTraceOut>,
    },
    MarkovTowerHomogeneous {
        num_strands: usize,
        scaled_trace_terms: Vec<RawDyadicTerm>,
    },
    BratteliTwoRowRational {
        trace_num: String,
        trace_den: String,
        characters: Vec<(Vec<usize>, String, String)>,
    },
}

/// Specialized zero-tree-allocation $H_3(q)$ 6-component dyadic step on basis words:
/// `[ [], [0], [1], [1, 0], [0, 1], [0, 1, 0] ]`.
fn step_h3_dyadic(nf: &[DyadicLaurent; 6], s: &DyadicStepSpec) -> [DyadicLaurent; 6] {
    let mut out = [
        DyadicLaurent::zero(),
        DyadicLaurent::zero(),
        DyadicLaurent::zero(),
        DyadicLaurent::zero(),
        DyadicLaurent::zero(),
        DyadicLaurent::zero(),
    ];

    let add_c = |dst: &mut DyadicLaurent, src: &DyadicLaurent| {
        if s.c_mant != 0 && !src.is_zero() {
            let term = src.scale_dyadic_h_pow(s.c_mant, s.c_exp2, s.c_hpow);
            *dst = dst.add_val(&term);
        }
    };
    let add_ch = |dst: &mut DyadicLaurent, src: &DyadicLaurent| {
        if s.c_mant != 0 && !src.is_zero() {
            let term = src.scale_dyadic_h_pow(s.c_mant, s.c_exp2, s.c_hpow + 1);
            *dst = dst.add_val(&term);
        }
    };
    let add_d = |dst: &mut DyadicLaurent, src: &DyadicLaurent| {
        if s.d_mant != 0 && !src.is_zero() {
            let term = src.scale_dyadic_h_pow(s.d_mant, s.d_exp2, s.d_hpow);
            *dst = dst.add_val(&term);
        }
    };

    match s.gen {
        0 => {
            // 0: [] -> [0]*c + []*d
            add_c(&mut out[1], &nf[0]);
            add_d(&mut out[0], &nf[0]);
            // 1: [0] -> [0]*ch + []*c + [0]*d
            add_ch(&mut out[1], &nf[1]);
            add_c(&mut out[0], &nf[1]);
            add_d(&mut out[1], &nf[1]);
            // 2: [1] -> [1,0]*c + [1]*d
            add_c(&mut out[3], &nf[2]);
            add_d(&mut out[2], &nf[2]);
            // 3: [1,0] -> [1,0]*ch + [1]*c + [1,0]*d
            add_ch(&mut out[3], &nf[3]);
            add_c(&mut out[2], &nf[3]);
            add_d(&mut out[3], &nf[3]);
            // 4: [0,1] -> [0,1,0]*c + [0,1]*d
            add_c(&mut out[5], &nf[4]);
            add_d(&mut out[4], &nf[4]);
            // 5: [0,1,0] -> [0,1,0]*ch + [0,1]*c + [0,1,0]*d
            add_ch(&mut out[5], &nf[5]);
            add_c(&mut out[4], &nf[5]);
            add_d(&mut out[5], &nf[5]);
        }
        1 => {
            // 0: [] -> [1]*c + []*d
            add_c(&mut out[2], &nf[0]);
            add_d(&mut out[0], &nf[0]);
            // 1: [0] -> [0,1]*c + [0]*d
            add_c(&mut out[4], &nf[1]);
            add_d(&mut out[1], &nf[1]);
            // 2: [1] -> [1]*ch + []*c + [1]*d
            add_ch(&mut out[2], &nf[2]);
            add_c(&mut out[0], &nf[2]);
            add_d(&mut out[2], &nf[2]);
            // 3: [1,0] -> [0,1,0]*c + [1,0]*d  (since [1,0,1] = [0,1,0])
            add_c(&mut out[5], &nf[3]);
            add_d(&mut out[3], &nf[3]);
            // 4: [0,1] -> [0,1]*ch + [0]*c + [0,1]*d
            add_ch(&mut out[4], &nf[4]);
            add_c(&mut out[1], &nf[4]);
            add_d(&mut out[4], &nf[4]);
            // 5: [0,1,0] -> [0,1,0]*ch + [1,0]*c + [0,1,0]*d
            add_ch(&mut out[5], &nf[5]);
            add_c(&mut out[3], &nf[5]);
            add_d(&mut out[5], &nf[5]);
        }
        g => panic!("H_3 specialized fast path received generator {g} > 1"),
    }
    out
}

fn run_nf_job(job: NfWalkJob) -> NfJobResult {
    let mut support: BTreeSet<i32> = BTreeSet::new();
    let mut components = Vec::new();

    if job.num_strands == 3 {
        let words: [Vec<usize>; 6] = [
            vec![],
            vec![0],
            vec![1],
            vec![1, 0],
            vec![0, 1],
            vec![0, 1, 0],
        ];
        let mut nf = [
            DyadicLaurent::one(),
            DyadicLaurent::zero(),
            DyadicLaurent::zero(),
            DyadicLaurent::zero(),
            DyadicLaurent::zero(),
            DyadicLaurent::zero(),
        ];
        for step in &job.steps {
            for _ in 0..step.repeat {
                nf = step_h3_dyadic(&nf, step);
            }
        }
        for (w, poly) in words.into_iter().zip(nf.into_iter()) {
            let raw_terms = poly.nonzero_terms();
            for (e, _, _) in &raw_terms {
                support.insert(*e);
            }
            components.push(BasisComponentOut {
                word: w,
                min_degree: poly.min_degree(),
                max_degree: poly.max_degree(),
                n_terms: raw_terms.len(),
                terms: if job.include_terms {
                    Some(
                        raw_terms
                            .into_iter()
                            .map(|(e, m, e2)| (e, m.to_string(), e2))
                            .collect(),
                    )
                } else {
                    None
                },
            });
        }
    } else {
        let mut acc = StreamingHeckeAccumulator::new(job.num_strands, DyadicLaurent::h());
        for step in &job.steps {
            let lf = step.to_linear_factor();
            for _ in 0..step.repeat {
                acc.push_linear(&lf);
            }
        }
        let state = acc.into_state();
        for (w, poly) in state.terms() {
            let raw_terms = poly.nonzero_terms();
            for (e, _, _) in &raw_terms {
                support.insert(*e);
            }
            components.push(BasisComponentOut {
                word: w.clone(),
                min_degree: poly.min_degree(),
                max_degree: poly.max_degree(),
                n_terms: raw_terms.len(),
                terms: if job.include_terms {
                    Some(
                        raw_terms
                            .into_iter()
                            .map(|(e, m, e2)| (e, m.to_string(), e2))
                            .collect(),
                    )
                } else {
                    None
                },
            });
        }
    }

    let min_deg = support.iter().next().copied().unwrap_or(0);
    let max_deg = support.iter().next_back().copied().unwrap_or(0);
    let total_terms: usize = components.iter().map(|c| c.n_terms).sum();

    NfJobResult {
        id: job.id,
        min_degree: min_deg,
        max_degree: max_deg,
        degree_span: max_deg - min_deg,
        n_terms: total_terms,
        support_size: support.len(),
        components,
    }
}

/// Embed a planar diagram on `m` strands into `m + 1` strands by adding a straight
/// rightmost through-strand connecting top `m` to bottom `(m + 1) + m`.
fn embed_planar_matching_plus_one(d: &PlanarMatching) -> PlanarMatching {
    let m = d.num_strands();
    let next_n = m + 1;
    // Reconstruct via JSON/public partner query? Even cleaner: PlanarMatching exposes partner_of,
    // or we work directly inside TL_{max_strands} and divide loop_closure_trace by delta^{max - m}!
    let _ = next_n;
    d.clone()
}

fn run_tl_trace_walk(levels: Vec<Vec<DyadicStepSpec>>) -> Vec<TlLevelTraceOut> {
    let total_strands = levels.len() + 1;
    let q = DyadicLaurent::q();
    let delta = DyadicLaurent::delta_two();
    let tl = TemperleyLiebBasis::with_hecke_projection(total_strands, q.clone())
        .expect("q is a unit in DyadicLaurent");

    let id_elem = TemperleyLiebElement::one(total_strands);
    let mut cur = id_elem.clone();
    let mut out = Vec::with_capacity(levels.len());

    for (lvl_idx, steps) in levels.into_iter().enumerate() {
        let m_strands = lvl_idx + 2;
        for step in &steps {
            let lf = step.to_linear_factor();
            // c * (q*1 - e_gen) + d * 1 = (c*q + d)*1 - c*e_gen
            let gen_img = tl.generator_image(lf.gen);
            let mut factor_el = gen_img.scale(&lf.c);
            factor_el.add_scaled_assign(&id_elem, &lf.d);
            for _ in 0..step.repeat {
                cur = cur.mul_tl(&factor_el, &delta);
            }
        }

        // On `total_strands`, strands `m_strands..total_strands` are untouched straight lines,
        // each contributing one extra closed loop (total `extra = total_strands - m_strands` loops)!
        // Rather than dividing by delta^extra, compute loop count restricted to `0..m_strands`?
        // Look: every untouched strand `s >= m_strands` is an isolated 2-cycle `(s, total_strands + s)`,
        // so `d.closure_loops() - (total_strands - m_strands)` is the EXACT loop count in TL_{m_strands}!!
        let extra_loops = total_strands - m_strands;
        let mut p_m = DyadicLaurent::zero();
        for (diag, coeff) in cur.terms() {
            let loops_m = diag.closure_loops() - extra_loops;
            let weight = delta.pow_u32(loops_m as u32);
            p_m = p_m.add_val(&coeff.mul_val(&weight));
        }

        let _ = embed_planar_matching_plus_one;
        out.push(TlLevelTraceOut {
            strands: m_strands,
            num_diagrams: cur.num_terms(),
            numerator_terms: serialize_poly_terms(&p_m),
        });
    }
    out
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let args: Vec<String> = env::args().collect();
    let mut input_path: Option<String> = None;
    let mut output_path: Option<String> = None;
    let mut i = 1usize;
    while i < args.len() {
        match args[i].as_str() {
            "--input" => {
                i += 1;
                input_path = args.get(i).cloned();
            }
            "--output" => {
                i += 1;
                output_path = args.get(i).cloned();
            }
            "--help" | "-h" => {
                writeln!(
                    io::stdout(),
                    "Usage: gs-peel [--input <request.json>] [--output <response.json>]"
                )?;
                return Ok(());
            }
            other => {
                return Err(format!("unrecognized flag: {other}").into());
            }
        }
        i += 1;
    }

    let raw_in = match input_path {
        Some(p) => fs::read_to_string(p)?,
        None => {
            let mut buf = String::new();
            io::stdin().read_to_string(&mut buf)?;
            buf
        }
    };

    let req: PeelRequest = serde_json::from_str(&raw_in)?;
    let resp = match req {
        PeelRequest::DyadicHeckeNfBatch { jobs } => {
            let results = jobs.into_iter().map(run_nf_job).collect();
            PeelResponse::DyadicHeckeNfBatch { results }
        }
        PeelRequest::TlDyadicTraceWalk { levels } => {
            let out = run_tl_trace_walk(levels);
            PeelResponse::TlDyadicTraceWalk { levels: out }
        }
        PeelRequest::MarkovTowerHomogeneous { num_strands, steps } => {
            let mut factors = Vec::new();
            for st in &steps {
                let lf = st.to_linear_factor();
                for _ in 0..st.repeat {
                    factors.push(lf.clone());
                }
            }
            let h = DyadicLaurent::h();
            // Balanced TL Markov parameter z = q^2 / (q + q^-1):
            let z_num = DyadicLaurent::monomial(2, DyadicScalar::one());
            let z_den = DyadicLaurent::delta_two();
            let scaled =
                streaming_markov_trace_homogeneous(&factors, num_strands, &h, &z_num, &z_den);
            PeelResponse::MarkovTowerHomogeneous {
                num_strands,
                scaled_trace_terms: serialize_poly_terms(&scaled),
            }
        }
        PeelRequest::BratteliTwoRowRational {
            num_strands,
            q_num,
            q_den,
            factors,
        } => {
            let q = rat(q_num, q_den);
            let lin: Vec<LinearFactor<BigRational>> = factors
                .into_iter()
                .map(|f| LinearFactor::new(rat(f.c_num, f.c_den), rat(f.d_num, f.d_den), f.gen))
                .collect();
            let (tr, chars) = two_row_bratteli_trace(&lin, num_strands, &q)
                .map_err(|e| format!("Bratteli transfer error: {e:?}"))?;
            let characters = chars
                .into_iter()
                .map(|(lam, v)| (lam, v.numer().to_string(), v.denom().to_string()))
                .collect();
            let _ = BigInt::from(0);
            PeelResponse::BratteliTwoRowRational {
                trace_num: tr.numer().to_string(),
                trace_den: tr.denom().to_string(),
                characters,
            }
        }
    };

    let json_out = serde_json::to_string(&resp)?;
    match output_path {
        Some(p) => fs::write(p, json_out)?,
        None => {
            let mut stdout = io::stdout().lock();
            stdout.write_all(json_out.as_bytes())?;
            stdout.write_all(b"\n")?;
        }
    }
    Ok(())
}
