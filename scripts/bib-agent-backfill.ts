import { readFileSync, existsSync } from 'fs';
import { join } from 'path';
import { processIngestion } from '../pipeline/bib-photo-ingestion-watcher.js';

/**
 * bib-agent-backfill.ts
 * 
 * Implements Phase 4 of the Bib Human-Review workflow:
 * Identifies references mapped in `library/intake.json` that are currently 
 * 'unreviewed' or 'source-in-repo', and triggers the ingestion pipeline.
 */

const INTAKE_FILE = 'library/intake.json';
const REVIEWS_FILE = 'content/schema/references.review.json';

async function main() {
  if (!existsSync(INTAKE_FILE)) {
    console.error("No library/intake.json found.");
    return;
  }

  const intakeData = JSON.parse(readFileSync(INTAKE_FILE, 'utf8'));
  const targetRefId = intakeData.targetPaper || intakeData.id;

  if (!targetRefId) {
    console.error("intake.json has neither 'targetPaper' nor 'id'; nothing to backfill.");
    return;
  }

  console.log(`[Backfill] Analyzing intake.json for reference: ${targetRefId}`);

  let needsReview = true;
  if (existsSync(REVIEWS_FILE)) {
    const reviews = JSON.parse(readFileSync(REVIEWS_FILE, 'utf8'));
    const status = reviews.reviews[targetRefId]?.status;
    if (status === 'validated') {
      console.log(`[Backfill] Reference ${targetRefId} is already validated.`);
      needsReview = false;
    }
  }

  if (needsReview) {
    console.log(`[Backfill] Triggering ingestion for backfill reference: ${targetRefId}`);
    // Assume the PDF name matches the id in intake.json, falling back to targetRefId
    const pdfId = intakeData.id || targetRefId;
    const pdfPath = join('uploads', `${pdfId}.pdf`);
    if (existsSync(pdfPath)) {
      await processIngestion({
        type: 'local_backfill',
        filePath: pdfPath,
        referenceId: targetRefId
      });
    } else {
      console.error(`[Backfill] Error: Could not find PDF at ${pdfPath}`);
    }
  }

  console.log("[Backfill] Completed processing intake backlog.");
}

main().catch(console.error);
