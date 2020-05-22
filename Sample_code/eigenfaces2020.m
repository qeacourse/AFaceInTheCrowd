function accuracy = eigenfaces2020(numPrincipalComponents, useOnlyNoSmileForTraining, showEigenFaces)
% handy trick to set a default values for our arguments
if nargin < 1
    numPrincipalComponents = 10;
end
if nargin < 2
    % this is true to use the data in part 7
    useOnlyNoSmileForTraining = false;
end
if nargin < 3
    showEigenFaces = false;
end

if ~useOnlyNoSmileForTraining
    load('classdata_train.mat');
    load('classdata_test.mat');
else
    load('classdata_no_smile.mat');
    load('classdata_smile.mat');
end

ATrain = reshape(grayfaces_train, [size(grayfaces_train,1)*size(grayfaces_train,2), size(grayfaces_train,3)])';
ATest = reshape(grayfaces_test, [size(grayfaces_test,1)*size(grayfaces_test,2), size(grayfaces_test,3)])';

% mean center the train and test data
ATrain = ATrain - mean(ATrain);
ATest = ATest - mean(ATest);

% get covariance matrix of the training data
covar = ATrain'*ATrain;

% get EVD (so we can do PCA)
% If you want all of the Eigenvectors / Eigenvalue, you can use eig:
% [Q, Delta] = eig(covar);

% if you wan to just get the eigenvectors swith largest eigenvalues
% you can use eigs.
[Q, Delta] = eigs(covar, numPrincipalComponents);

if showEigenFaces
    % visualize the principal components as images
    f = figure;
    for i = 1 : numPrincipalComponents
        subplot(ceil(sqrt(numPrincipalComponents)), ceil(sqrt(numPrincipalComponents)), i);
        imagesc(reshape(Q(:,i), [64 64]));  % TODO: remove hardcoding
        colormap('gray');
    end
end

% project into face space
faceSpaceTrain = Q'*ATrain';
faceSpaceTest = Q'*ATest';

% Use nearest neighbor search (you can code this manually if you'd like)
NN = knnsearch(faceSpaceTrain', faceSpaceTest');

% let's check to see if the subject corresponding to the second closest
% photo is the same as the one corresponding to the query image
accuracy = mean(subject_train(NN)==subject_test);
end
