//! tl-cable-mpfr — batch CLI for the full-MPFR TL cable transfer engine
//! (`hecke_engine::tl_cable_mpfr`): raw colored-Jones J'_{cN+1} evaluations
//! via the Jones–Wenzl cN-cable at MPFR precision.
//!
//! One process handles a whole batch so the (expensive) TL engine build
//! is amortized across evaluations — the Python driver makes ONE
//! subprocess call per batch (the whole-compute-per-boundary-crossing
//! granularity rule of `.claude/skills/local/compute-author.md` §2.1).
//!
//! Input (stdin or --job FILE), JSON:
//! {
//!   "prec": 192,
//!   "jobs": [
//!     {"word": [1,1,1,2,-1,2], "k": 3, "cn": 5, "q": "1.109978..."},
//!     ...
//!   ]
//! }
//!
//! Output (stdout), JSON:
//! {"results": [{"jp": "<decimal>", "n": 15, "dim": 9694845, "secs": 12.3}, ...]}
//!
//! J' values are emitted as 40-significant-digit decimal strings.

use hecke_engine::tl_cable_mpfr::JpEvaluator;
use serde::{Deserialize, Serialize};
use std::collections::HashMap;
use std::io::Read;
use std::time::Instant;

#[derive(Deserialize)]
struct Job {
    word: Vec<i32>,
    k: usize,
    cn: usize,
    q: String,
}

#[derive(Deserialize)]
struct Batch {
    #[serde(default = "default_prec")]
    prec: u32,
    jobs: Vec<Job>,
}

fn default_prec() -> u32 {
    192
}

#[derive(Serialize)]
struct JobResult {
    jp: String,
    n: usize,
    dim: usize,
    secs: f64,
}

#[derive(Serialize)]
struct Output {
    results: Vec<JobResult>,
}

fn main() {
    let args: Vec<String> = std::env::args().collect();
    let text = if args.len() == 3 && args[1] == "--job" {
        std::fs::read_to_string(&args[2]).expect("cannot read job file")
    } else {
        let mut s = String::new();
        std::io::stdin()
            .read_to_string(&mut s)
            .expect("cannot read stdin");
        s
    };
    let batch: Batch = serde_json::from_str(&text).expect("bad job JSON");

    let mut evaluators: HashMap<(usize, usize), JpEvaluator> = HashMap::new();
    let mut results = Vec::with_capacity(batch.jobs.len());
    for (ji, job) in batch.jobs.iter().enumerate() {
        let key = (job.k, job.cn);
        let ev = evaluators.entry(key).or_insert_with(|| {
            let t = Instant::now();
            let ev = JpEvaluator::new(job.k, job.cn);
            eprintln!(
                "[tl-cable-mpfr] engine n={} (dim {}) built in {:.1}s",
                ev.big.n,
                ev.big.dim,
                t.elapsed().as_secs_f64()
            );
            ev
        });
        let t = Instant::now();
        let jp = ev.jp(&job.word, &job.q, batch.prec);
        let secs = t.elapsed().as_secs_f64();
        eprintln!(
            "[tl-cable-mpfr] job {}/{}: n={} q={}… done in {:.1}s",
            ji + 1,
            batch.jobs.len(),
            ev.big.n,
            &job.q[..job.q.len().min(8)],
            secs
        );
        results.push(JobResult {
            jp: jp.to_string_radix(10, Some(40)),
            n: ev.big.n,
            dim: ev.big.dim,
            secs,
        });
    }
    println!(
        "{}",
        serde_json::to_string(&Output { results }).expect("serialize")
    );
}
