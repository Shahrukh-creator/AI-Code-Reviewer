import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { CodeReviewService } from '../../services/code-review.service';
import { ReviewResponse } from '../../models/code-review.model';

@Component({
  selector: 'app-code-reviewer',
  standalone: true,
  imports: [
    CommonModule,
    FormsModule,
  ],
  templateUrl: './code-reviewer.component.html',
  styleUrl: './code-reviewer.component.css',
})
export class CodeReviewerComponent {
  language = 'python';

  code = `def get_user(user_id):
    query = "SELECT * FROM users WHERE id = " + user_id

    try:
        result = database.execute(query)
        return result
    except:
        pass`;

  result: ReviewResponse | null = null;

  loading = false;
  errorMessage = '';

  constructor(
    private codeReviewService: CodeReviewService
  ) {}

  reviewCode(): void {
    if (!this.code.trim()) {
      this.errorMessage = 'Please enter code to review.';
      return;
    }

    this.loading = true;
    this.errorMessage = '';
    this.result = null;

    this.codeReviewService.reviewCode({
      language: this.language,
      code: this.code,
    }).subscribe({
      next: (response) => {
        this.result = response;
        this.loading = false;
      },
      error: (error) => {
        console.error(error);

        this.errorMessage =
          error?.error?.detail ||
          'Code review failed. Please try again.';

        this.loading = false;
      },
    });
  }

  getSeverityClass(severity: string): string {
    return `severity-${severity.toLowerCase()}`;
  }
}