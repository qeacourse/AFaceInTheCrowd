accuracies = zeros(100,1);
% this could be sped up dramatically if you just compute the Eigenvectors once
for numComponents = 1:100
    numComponents % don't supress output so we can see progress
    % add set the second argument of `eigenfaesc2020` to true to use non
    % smiles for training and smiles for testing
    accuracies(numComponents) = eigenfaces2020(numComponents);
end

plot(accuracies);
xlabel('Number of principal components');
ylabel('Accuracy');