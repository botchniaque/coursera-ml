function plotData(X, y)
%PLOTDATA Plots the data points X and y into a new figure 
%   PLOTDATA(x,y) plots the data points with + for the positive examples
%   and o for the negative examples. X is assumed to be a Mx2 matrix.

% Create New Figure
figure; hold on;

% ====================== YOUR CODE HERE ======================
% Instructions: Plot the positive and negative examples on a
%               2D plot, using the option 'k+' for the positive
%               examples and 'ko' for the negative examples.
%

a = [X, y];
zeros = a(a(:, 3)==0, :);
ones = a(a(:, 3)==1, :);

plot(ones(:, 1), ones(:, 2), 'k+')
hold on;
plot(zeros(:, 1), zeros(:, 2), 'yo', 'MarkerEdgeColor', 'black', 'MarkerFaceColor', 'yellow')
hold on;


% =========================================================================



hold off;

end
