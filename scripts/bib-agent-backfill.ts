import { readFileSync, writeFileSync, existsSync } from 'fs';
import { join } from 'path';
import { processIngestion } from '../pipeline/bib-photo-ingestion-watcher.js';
import { references } from '../content/schema/references.js';
import { entryHash } from '../content/pipeline/validate-references-human-review.js';

/**
 * bib-agent-backfill.ts
 * 
 * Implements Phase 4 of the Bib Human-Review workflow:
 * Identifies references mapped in `uploads/intake.json` that are currently 
 * 'unreviewed' or 'source-in-repo', and triggers the ingestion pipeline.
 */

const INTAKE_FILE = 'uploads/intake.json';
const REVIEWS_FILE = 'content/schema/references.review.json';

async function main() {
  if (!existsSync(INTAKE_FILE)) {
    console.error("No uploads/intake.json found.");
    return;
  }

  const intakeData = JSON.parse(readFileSync(INTAKE_FILE, 'utf8'));
  const targetRefId = intakeData.targetPaper || intakeData.id;

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
    // Assume the PDF name matches the id in intake.json
    const pdfPath = join('uploads', `${intakeData.id}.pdf`);
    if (existsSync(pdfPath)) {
      await processIngestion({
        type: 'local_backfill',
        filePath: pdfPath,
        referenceId: targetRefId
      });

      // Update the hash properly after processIngestion since processIngestion uses 'pending'
      const entry = references.find(r => r.id === targetRefId);
      if (entry && existsSync(REVIEWS_FILE)) {
         const hash = entryHash(entry);
         const reviews = JSON.parse(readFileSync(REVIEWS_FILE, 'utf8'));
         if (reviews.reviews[targetRefId]) {
             reviews.reviews[targetRefId].entryHash = hash;
             writeFileSync(REVIEWS_FILE, JSON.stringify(reviews, null, 2));
             console.log(`[Backfill] Updated proper entryHash ${hash} for ${targetRefId}`);
         }
      }

    } else {
      console.error(`[Backfill] Error: Could not find PDF at ${pdfPath}`);
    }
  }

  console.log("[Backfill] Completed processing intake backlog.");
}

main().catch(console.error);
