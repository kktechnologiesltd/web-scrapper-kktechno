// Import the Cheerio library
const cheerio = require('cheerio')
const fs = require('fs');
// Load the HTML code as a string, which returns a Cheerio instance


// We can use the same API as jQuery to get the desired result
function readFiles(dirname, onFileContent, onError) {
    fs.readdir(dirname, function(err, filenames) {
        if (err) {
            onError(err);
            return;
        }
        filenames.forEach(function(filename) {
            fs.readFile(dirname + filename, 'utf-8', function(err, content) {
                if (err) {
                    onError(err);
                    return;
                }
                onFileContent(filename, content);
            });
        });
    });
}

function onFileContent(filename, content) {
    const $ = cheerio.load(fs.readFileSync('contents/'+filename));
}
var data = {};
readFiles('contents/', function(filename, content) {
    //console.log(filename,content);
    $ = cheerio.load(content);
    $('img').each(function(){
       console.log("HERE",$(this).attr("src"))
    })
    //data[filename] = content;
    $ = null
}, function(err) {
    throw err;
});