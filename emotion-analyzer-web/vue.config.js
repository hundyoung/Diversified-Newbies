var path = require('path');
function resolve(dir) {
    return path.join(__dirname, dir);
}

module.exports = {
    publicPath: process.env.NODE_ENV === 'production' ? '/' : '/',
    lintOnSave: process.env.NODE_ENV !== 'production',
    chainWebpack: config => {
        config.resolve.alias
            .set('@', resolve('src'))
            .set('_config', resolve('src/config'))
            .set('_components', resolve('src/components'))
            .set('_frame', resolve('src/frame'))
            .set('_views', resolve('src/views'));
    },
    productionSourceMap: false,
    css: {
        loaderOptions: {
            less: {
                javascriptEnabled: true
            }
        }
    }
};
