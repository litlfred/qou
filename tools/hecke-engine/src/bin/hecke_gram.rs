//! `hecke gram` — print the H_3(q) Gram matrix and its inverse as JSON.
//!
//! Usage::
//!
//!     hecke-gram                      # default q_0
//!     hecke-gram --q 1.2              # custom q
//!     hecke-gram --q 1.1099785955541805 --pretty
//!     hecke-gram --schema             # print the JSON Schema
//!
//! Output matches the `gram.schema.json` at
//! `tools/hecke-engine/schemas/gram.schema.json`.

use hecke_engine::{gram, nf};

fn print_usage(stream_stderr: bool) {
    let text = format!(
        "hecke-gram [--q Q] [--pretty] [--schema]\n\
         \n\
         Options:\n  \
         --q Q       substrate parameter (default: {})\n  \
         --pretty    indent JSON output\n  \
         --schema    print the JSON Schema and exit\n  \
         --help      this message",
        nf::Q_0
    );
    if stream_stderr {
        eprintln!("{text}");
    } else {
        println!("{text}");
    }
}

fn main() {
    let mut q = nf::Q_0;
    let mut pretty = false;
    let mut schema = false;
    let mut args = std::env::args().skip(1);
    while let Some(arg) = args.next() {
        match arg.as_str() {
            "--q" => {
                q = args
                    .next()
                    .and_then(|s| s.parse::<f64>().ok())
                    .unwrap_or_else(|| {
                        eprintln!("--q requires a numeric argument");
                        std::process::exit(2);
                    });
            }
            "--pretty" => pretty = true,
            "--schema" => schema = true,
            "--help" | "-h" => {
                // Help goes to stdout + exit 0 per POSIX convention.
                print_usage(false);
                std::process::exit(0);
            }
            other => {
                eprintln!("unknown argument: {other}");
                print_usage(true);
                std::process::exit(2);
            }
        }
    }

    if schema {
        let s = include_str!("../../schemas/gram.schema.json");
        println!("{s}");
        return;
    }

    let cert = gram::certificate_at(q);
    let out = if pretty {
        serde_json::to_string_pretty(&cert)
    } else {
        serde_json::to_string(&cert)
    };
    match out {
        Ok(s) => println!("{s}"),
        Err(e) => {
            eprintln!("serialization error: {e}");
            std::process::exit(1);
        }
    }
}
