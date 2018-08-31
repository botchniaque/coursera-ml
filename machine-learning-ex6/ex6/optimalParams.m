load('ex6data3.mat');

Cs = [0.01, 0.03, 0.1, 0.3, 1, 3, 10, 30]
sigmas = [0.01, 0.03, 0.1, 0.3, 1, 3, 10, 30]

sizeC = size(Cs, 2)
sizeSigma = size(sigmas, 2)

result = zeros(sizeC * sizeSigma, 3);

k = 0

for i = 1:sizeC
    for j = 1:sizeSigma
        C = Cs(i);
        sigma = sigmas(j);
        model= svmTrain(X, y, C, @(x1, x2) gaussianKernel(x1, x2, sigma));

        predictions = svmPredict(model, Xval);
        error = mean(double(predictions ~= yval));
        k = (i-1)*sizeC + j;
        result(k, :) = [C, sigma, error];
    end
end

result

[val, ind] = min(result, [], 1);

result(ind(3), :)