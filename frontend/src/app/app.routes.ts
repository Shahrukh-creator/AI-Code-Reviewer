import { Routes } from '@angular/router';

export const routes: Routes = [
  {
    path: '',
    loadComponent: () =>
      import('./features/code-reviewer/code-reviewer.component')
        .then(m => m.CodeReviewerComponent),
  },
  {
    path: '**',
    redirectTo: '',
  },
];