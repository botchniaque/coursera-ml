function [theta, J_history] = gradientDescentMulti(X, y, theta, alpha, num_iters)
%GRADIENTDESCENTMULTI Performs gradient descent to learn theta
%   theta = GRADIENTDESCENTMULTI(x, y, theta, alpha, num_iters) updates theta by
%   taking num_iters gradient steps with learning rate alpha

% Initialize some useful values
m = length(y); % number of training examples
J_history = zeros(num_iters, 1);

for iter = 1:num_iters

    % ====================== YOUR CODE HERE ======================
    % Instructions: Perform a single gradient step on the parameter vector
    %               theta. 
    %
    % Hint: While debugging, it can be useful to print out the values
    %       of the cost function (computeCostMulti) and gradient here.
    %



    A = [0 0; alpha 0; 0 alpha; alpha alpha; -alpha 0; 0 -alpha; -alpha -alpha ]'

    T = theta + A


    c1 = computeCost(X, y, T(:,1))
    c2 = computeCost(X, y, T(:,2))
    c3 = computeCost(X, y, T(:,3))
    c4 = computeCost(X, y, T(:,4))
    c5 = computeCost(X, y, T(:,5))
    c6 = computeCost(X, y, T(:,6))
    c7 = computeCost(X, y, T(:,7))

    [x, ix] = min([c1, c2, c3, c4, c5, c6, c7])
    theta = T(:, ix)

    % ============================================================

    % Save the cost J in every iteration
    J_history(iter) = x;

end

end
