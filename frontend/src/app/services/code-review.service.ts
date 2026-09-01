import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

import {
  ReviewRequest,
  ReviewResponse,
} from '../models/code-review.model';

@Injectable({
  providedIn: 'root',
})
export class CodeReviewService {

  private readonly apiUrl = 'http://localhost:8000/api/review';

  constructor(private http: HttpClient) {}

  reviewCode(request: ReviewRequest): Observable<ReviewResponse> {
    return this.http.post<ReviewResponse>(
      this.apiUrl,
      request
    );
  }
}