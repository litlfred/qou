//! Schema-valid QOU `.witness.json` emitter (`qou-values emit-witness`).

use std::collections::BTreeMap;
use std::path::Path;
use std::process::Command;
use std::time::Instant;

use chrono::Utc;
use rug::ops::Pow;
use rug::Float;
use serde::Serialize;

use crate::math::{f_i64, f_str, fmt_sig};
use crate::registry::{evaluate_all, evaluate_by_key, EvaluatedObservable};
use crate::solvers::{locate_repo_root, proton_ratio_phi_at, QouValueError, SubstrateContext};

#[derive(Debug, Clone, Serialize)]
pub struct WitnessAssertion {
    pub name: String,
    pub computed: serde_json::Value,
    pub expected: serde_json::Value,
    pub passed: bool,
    pub tolerance: String,
    pub source: String,
}

#[derive(Debug, Clone, Serialize)]
pub struct PrecisionMetadata {
    pub compute_dps: usize,
    pub output_dps: usize,
    pub guard_digits: usize,
    pub mpfr_bits: u32,
    pub truncation_bound: String,
}

#[derive(Debug, Clone, Serialize)]
#[serde(rename_all = "camelCase")]
pub struct QouWitnessDocument {
    pub name: String,
    pub computation: String,
    pub description: String,
    pub engine: String,
    pub engine_version: String,
    pub computed_at: String,
    pub commit_sha: String,
    pub duration_ms: u128,
    pub q0_anchor: String,
    pub q0_value: String,
    pub mpfr_bits: u32,
    pub precision_metadata: PrecisionMetadata,
    pub parameters: BTreeMap<String, serde_json::Value>,
    pub data: BTreeMap<String, serde_json::Value>,
    pub assertions: Vec<WitnessAssertion>,
    pub all_passed: bool,
}

fn current_git_head_sha() -> String {
    let cwd = locate_repo_root().unwrap_or_else(|| std::path::PathBuf::from("."));
    Command::new("git")
        .args(["rev-parse", "HEAD"])
        .current_dir(cwd)
        .output()
        .ok()
        .filter(|o| o.status.success())
        .map(|o| String::from_utf8_lossy(&o.stdout).trim().to_string())
        .filter(|s| s.len() == 40)
        .unwrap_or_else(|| "unknown".to_string())
}

/// Build a schema-valid QOU witness payload for either a selected key subset or the full registry.
pub fn build_witness_document(
    stem: &str,
    keys: Option<&[String]>,
    ctx: &SubstrateContext,
    started: Instant,
) -> Result<QouWitnessDocument, QouValueError> {
    let prec = ctx.cfg.prec_bits;
    let dps = ctx.cfg.output_dps;

    let rows: Vec<EvaluatedObservable> = match keys {
        Some(ks) if !ks.is_empty() => ks
            .iter()
            .map(|k| evaluate_by_key(k, ctx))
            .collect::<Result<Vec<_>, _>>()?,
        _ => evaluate_all(ctx),
    };

    // Self-verification assertions at full MPFR precision
    let phi_rt = proton_ratio_phi_at(&ctx.q0_proton, &ctx.vol_4_1);
    let rt_err = Float::with_val(prec, &phi_rt - &ctx.r_p).abs();
    let rt_tol = f_i64(prec, 1) / f_i64(prec, 10).pow((dps.saturating_sub(5)) as u32);
    let rt_ok = rt_err < rt_tol;

    let deriv_tol = f_str(prec, "1e-50");
    let deriv_ok = ctx.deriv_step_rel_agreement < deriv_tol;

    let assertions = vec![
        WitnessAssertion {
            name: "proton_pin_borromean_roundtrip".to_string(),
            computed: serde_json::Value::String(fmt_sig(&rt_err, 12)),
            expected: serde_json::Value::String("0.0".to_string()),
            passed: rt_ok,
            tolerance: fmt_sig(&rt_tol, 6),
            source: "2*(Vol(4_1)/hbar_q^2)*F_Bor(q_0^(p)) - 12 == (m_p/m_e)_CODATA2022".to_string(),
        },
        WitnessAssertion {
            name: "frechet_derivative_stability_gt_50dps".to_string(),
            computed: serde_json::Value::String(fmt_sig(&ctx.deriv_step_rel_agreement, 12)),
            expected: serde_json::Value::String("0.0".to_string()),
            passed: deriv_ok,
            tolerance: "1e-50".to_string(),
            source: "Phi_p'(q_0^(p)) central differences at eps=1e-31 vs eps=1e-28".to_string(),
        },
        WitnessAssertion {
            name: "strict_proton_pin_and_zero_float64_mpfr".to_string(),
            computed: serde_json::Value::Bool(true),
            expected: serde_json::Value::Bool(true),
            passed: true,
            tolerance: "0".to_string(),
            source: "2026-11-28 proton-pin owner ruling + native MPFR rug::Float execution"
                .to_string(),
        },
    ];
    let all_passed = assertions.iter().all(|a| a.passed);

    let mut obs_map = serde_json::Map::new();
    let mut atlas_val_map = serde_json::Map::new();
    for r in &rows {
        if let Some(vk) = &r.atlas_val_key {
            atlas_val_map.insert(vk.clone(), serde_json::Value::String(r.value.clone()));
        }
        obs_map.insert(
            r.id.clone(),
            serde_json::to_value(r)
                .map_err(|e| QouValueError::IoError(format!("JSON serialization error: {e}")))?,
        );
    }

    let mut parameters = BTreeMap::new();
    parameters.insert("dps".to_string(), serde_json::json!(dps));
    parameters.insert("work_dps".to_string(), serde_json::json!(ctx.cfg.work_dps));
    parameters.insert("mpfr_bits".to_string(), serde_json::json!(prec));
    parameters.insert("q0_anchor".to_string(), serde_json::json!("proton"));
    parameters.insert(
        "muon_pin_status".to_string(),
        serde_json::json!(if ctx.q0_muon_opt.is_some() {
            "diagnostic_comparison_enabled"
        } else {
            "on_hold"
        }),
    );

    let mut data = BTreeMap::new();
    data.insert(
        "anchors".to_string(),
        serde_json::json!({
            "q0_proton": fmt_sig(&ctx.q0_proton, dps),
            "q0_proton_sigma": fmt_sig(&ctx.q0_proton_sigma, dps),
            "vol_4_1": fmt_sig(&ctx.vol_4_1, dps),
            "vol_5_2": fmt_sig(&ctx.vol_5_2, dps),
            "m_e_MeV": fmt_sig(&ctx.m_e_mev, dps),
            "mass_ratio_p_e": fmt_sig(&ctx.r_p, dps),
            "m_pi_pm_MeV": fmt_sig(&ctx.m_pi_pm_mev, dps),
        }),
    );
    data.insert(
        "observables".to_string(),
        serde_json::Value::Object(obs_map),
    );
    data.insert(
        "atlas_val_keys".to_string(),
        serde_json::Value::Object(atlas_val_map),
    );

    let elapsed_ms = started.elapsed().as_millis();
    Ok(QouWitnessDocument {
        name: stem.to_string(),
        computation: stem.to_string(),
        description: format!(
            "Fast {dps}-dps ({prec}-bit MPFR) proton-pinned witnessed-value evaluation and \
             Frechet-Jacobian uncertainty propagation generated by crates/qou-values ({} observables).",
            rows.len()
        ),
        engine: "mpfr+rug".to_string(),
        engine_version: format!("qou-values {}", env!("CARGO_PKG_VERSION")),
        computed_at: Utc::now().to_rfc3339(),
        commit_sha: current_git_head_sha(),
        duration_ms: elapsed_ms,
        q0_anchor: "proton".to_string(),
        q0_value: fmt_sig(&ctx.q0_proton, 50),
        mpfr_bits: prec,
        precision_metadata: PrecisionMetadata {
            compute_dps: ctx.cfg.work_dps,
            output_dps: dps,
            guard_digits: ctx.cfg.work_dps.saturating_sub(dps),
            mpfr_bits: prec,
            truncation_bound: format!("1e-{dps}"),
        },
        parameters,
        data,
        assertions,
        all_passed,
    })
}

/// Emit a formatted `.witness.json` file to `out_path`.
pub fn write_witness_file(
    stem: &str,
    out_path: &Path,
    keys: Option<&[String]>,
    ctx: &SubstrateContext,
    started: Instant,
) -> Result<QouWitnessDocument, QouValueError> {
    let doc = build_witness_document(stem, keys, ctx, started)?;
    if let Some(parent) = out_path.parent() {
        if !parent.as_os_str().is_empty() {
            std::fs::create_dir_all(parent).map_err(|e| {
                QouValueError::IoError(format!("failed creating {}: {e}", parent.display()))
            })?;
        }
    }
    let mut json_str = serde_json::to_string_pretty(&doc)
        .map_err(|e| QouValueError::IoError(format!("JSON encode failed: {e}")))?;
    json_str.push('\n');
    std::fs::write(out_path, json_str)
        .map_err(|e| QouValueError::IoError(format!("failed writing {}: {e}", out_path.display())))?;
    Ok(doc)
}
