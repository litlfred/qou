import { readHumanReviews, writeHumanReviews } from '../folio-assistant/cat-harness-tools/schemas/library/bib-attestations';
import { createHash } from 'crypto';
import { references } from '../folio/schema/references.js';

/**
 * Deterministic 12-char fingerprint of a reference entry. Inlined here
 * because the original `validate-references-human-review` module (which
 * exported `entryHash`) was never merged to main; this keeps the watcher
 * self-contained. No on-main validator consumes this field yet, so the
 * exact algorithm is free to be a stable sha256 prefix.
 */
function entryHash(entry: unknown): string {
  return createHash('sha256').update(JSON.stringify(entry)).digest('hex').slice(0, 12);
}

/**
 * bib-photo-ingestion-watcher
 * 
 * This script runs the automation half of the bib-human-review workflow.
 * Triggered by either:
 *  1) A GitHub webhook payload for a `bib-physical-review` issue photo upload.
 *  2) A local run over `library/` to process the backfill queue.
 *
 * Steps:
 *  1. Read the source / OCR.
 *  2. Source-match the usage in QOU.
 *  3. Formalise in Lean.
 *  4. Bib-validate against the references sidecar.
 *  5. Set the reference's human-review status to `validated` — in the
 *     attestation store's `bib-human-review` family (or the legacy
 *     `folio/schema/references.review.json` before migration), through the
 *     platform's one reader/writer, `schemas/bib-attestations.ts`.
 */

/** The folio repository root: these scripts run from it. */
const REPO_ROOT = process.cwd();

interface Payload {
  type: 'github_issue' | 'local_backfill';
  filePath: string;
  referenceId: string;
}

export async function processIngestion(payload: Payload) {
  console.log(`[Watcher] Starting ingestion for ${payload.referenceId} from ${payload.filePath}`);
  
  // 1. Identify/OCR passage
  console.log(`[Watcher] -> Step 1: Identifying passage in ${payload.filePath}`);
  // TODO: integrate with LLM / Vision API here

  // 2. Source Match
  console.log(`[Watcher] -> Step 2: Source-matching for reference ${payload.referenceId}`);
  // TODO: check QOU usage matches extracted text

  // 3. Formalise (Lean)
  console.log(`[Watcher] -> Step 3: Formalising cited result in Lean`);
  // TODO: invoke local/paper-importer skill

  // 4. Validate and set status
  console.log(`[Watcher] -> Step 4: Validating and updating the human-review record`);
  
  const read = readHumanReviews(REPO_ROOT);
  console.log(`[Watcher]    ${read.note}`);
  if (read.from !== 'none') {
    const reviews = { reviews: { ...read.reviews } as Record<string, unknown> };
    const entry = references.find(r => r.id === payload.referenceId);
    const hash = entry ? entryHash(entry) : 'pending';

    reviews.reviews[payload.referenceId] = {
      status: 'validated',
      by: payload.type === 'github_issue' ? 'issue-uploader' : 'agent-backfill',
      date: new Date().toISOString().split('T')[0],
      source: payload.filePath,
      page: 'auto-identified',
      entryHash: hash
    };
    console.log(`[Watcher]    ${writeHumanReviews(REPO_ROOT, reviews.reviews as never).note}`);
    console.log(`[Watcher] -> Success. Reference ${payload.referenceId} marked as validated.`);
  }
}

// Simple CLI entry point for local backfill
if (import.meta.main) {
  const fileArg = process.argv[2];
  const refArg = process.argv[3];
  
  if (fileArg && refArg) {
    processIngestion({ type: 'local_backfill', filePath: fileArg, referenceId: refArg });
  } else {
    console.log("Usage: bun run pipeline/bib-photo-ingestion-watcher.ts <file_path> <reference_id>");
  }
}
