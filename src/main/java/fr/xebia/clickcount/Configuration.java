package fr.xebia.clickcount;

import javax.inject.Singleton;

@Singleton
public class Configuration {

    public final String redisHost;
    public final int redisPort;
    public final int redisConnectionTimeout;  //milliseconds

    public Configuration() {
        String _redisHost = "redis";
        int    _redisPort = 6379;

        try {
            String envVarStr;

            // Get the redis host address in an env var is it exists,
            // keep the default value otherwise.
            envVarStr = System.getenv( "XEBIA_CLICK_COUNT_REDIS_HOST" );
            if ( envVarStr != null )
                _redisHost = envVarStr;

            // Get the redis host port in an env var is it exists,
            // keep the default value otherwise.
            envVarStr = System.getenv( "XEBIA_CLICK_COUNT_REDIS_PORT" );
            if ( envVarStr != null )
                _redisPort = Integer.parseUnsignedInt( envVarStr );
        } catch ( Exception e ) {
        }
        finally {
            redisHost = _redisHost;
            redisPort = _redisPort;
            redisConnectionTimeout = 2000;
        }
    }
}
